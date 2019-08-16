import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib import error, request

host = "localhost"
port = 8080
routes = {
    '/api': 'http://127.0.0.1:5000',  # dev
    # '/api': '0.0.0.0:8000',  # prod
}


class SimpleHTTPProxy(SimpleHTTPRequestHandler):
    proxy_routes = {}

    @classmethod
    def set_routes(cls, proxy_routes):
        cls.proxy_routes = proxy_routes

    def do_GET(self):
        print("**", self.path)
        for root_from, root_to in self.proxy_routes.items():
            if self.path.startswith(root_from):
                url = root_to + self.path
                self.proxy_request(url)
            else:
                super().do_GET()

    def proxy_request(self, url):
        try:
            response = request.urlopen(url)
        except error.HTTPError as e:
            self.send_response_only(e.code)
            self.end_headers()
            return

        self.send_response_only(response.status)
        for name, value in response.headers.items():
            self.send_header(name, value)
        self.end_headers()
        self.copyfile(response, self.wfile)


SimpleHTTPProxy.set_routes(routes)

with HTTPServer((host, port), SimpleHTTPProxy) as httpd:
    host, port = httpd.socket.getsockname()
    print(f'Listening on http://{host}:{port}')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, exiting.")
        sys.exit(0)
