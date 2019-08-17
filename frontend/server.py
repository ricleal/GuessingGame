import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib import error, request

'''
Simple HTTP server and proxy based on the python http.server.HTTPServer
The proxy will make the http calls (original headers included) if the routes
match the key of the dictionary `routes`.
'''


# host and port where the server will run
host = "localhost"
port = 8080

# forward routes rules
routes = {
    # '/api': 'http://localhost:5000',  # dev
    '/api': 'http://localhost:8000',  # prod
}


class SimpleHTTPProxy(SimpleHTTPRequestHandler):
    proxy_routes = {}

    @classmethod
    def set_routes(cls, proxy_routes):
        cls.proxy_routes = proxy_routes

    def do_GET(self):
        for root_from, root_to in self.proxy_routes.items():
            if self.path.startswith(root_from):
                url = root_to + self.path
                print("Proxy forwarding from {} to {}".format(self.path, url))
                self.proxy_request(url)
            else:
                super().do_GET()

    def proxy_request(self, url):
        try:
            # Copy original headers (cookies are needed!!!)
            req = request.Request(url)
            for k, v in self.headers.items():
                req.add_header(k, v)
            response = request.urlopen(req)
        except error.HTTPError as e:
            self.send_response_only(e.code)
            self.end_headers()
            return

        self.send_response_only(response.status)
        for name, value in response.headers.items():
            self.send_header(name, value)
        self.end_headers()
        self.copyfile(response, self.wfile)


if __name__ == '__main__':

    dist_path = os.path.join(os.path.dirname(__file__), 'dist')
    os.chdir(dist_path)

    print("-------------------------- Routes ---------------------------")
    for root_from, root_to in routes.items():
        print(root_from, "-->", root_to)
    print("-------------------------------------------------------------")

    SimpleHTTPProxy.set_routes(routes)

    with HTTPServer((host, port), SimpleHTTPProxy) as httpd:
        host, port = httpd.socket.getsockname()
        print(f'Listening on http://{host}:{port}')
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nKeyboard interrupt received, exiting.")
            sys.exit(0)
