# GuessingGame

Guessing Game Problem

## Installation

### Backend

The backend is implemented in Python using Flask (an extensible web 
microframework for building web applications with Python).

**Requirements:**
- Python 3.6
- PIP
- Python Virtual Environment (`virtualenv`) is optional but recommended.

To deploy the app locally, first create a virtual environment and activate it(optional):

```sh
# virtualenv creation
virtualenv venv -p python3
# virtualenv activation
source venv/bin/activate
```

Install the requirements:
```sh
pip install -r requirements.txt
```

If not shipped, create a `.env` file (file with the definition of environment
variables used by the back end server).  See `env.base` for a template.
If the file / environment variable does not exist, the default argument 
(the second) of `os.getenv` is used. See `app/config.py` for more details.

**Development:**

Fire up the app in development:
```sh
python run_dev.py
```
To test go to: http://localhost:5000/api/start/1/10

Using the `curl` cookies feature one can play the game:

```sh
# create a game
curl -c /tmp/cookie_guess_game.txt -b /tmp/cookie_guess_game.txt  http://localhost:5000/api/start/1/10
# is it odd?
curl -c /tmp/cookie_guess_game.txt -b /tmp/cookie_guess_game.txt  http://localhost:5000/api/odd
# is it even?
curl -c /tmp/cookie_guess_game.txt -b /tmp/cookie_guess_game.txt  http://localhost:5000/api/even
# it it less than 4?
curl -c /tmp/cookie_guess_game.txt -b /tmp/cookie_guess_game.txt  http://localhost:5000/api/less/4
# it it greater than 5?
curl -c /tmp/cookie_guess_game.txt -b /tmp/cookie_guess_game.txt  http://localhost:5000/api/greater/6
# it it equal to 5?
curl -c /tmp/cookie_guess_game.txt -b /tmp/cookie_guess_game.txt  http://localhost:5000/api/guess/5
```

**Production:**

In production use `gunicorn` (you can also install and use `uWSGI` or other wsgi server):

```sh
# Example
# gunicorn -w <number of workers> --bind <IP>:<port> run_prod:app
# E.g.:
gunicorn -w 2 --bind localhost:8000 run_prod:app
```

To test: http://localhost:8000/api/start/1/10

In either case you should get a json with:
```json
{
  "success": true
}
```

**To run the tests:**

Type in the console

```sh
cd GuessingGame/backend
pytest -v
```

The result should be similar to this:
```
============================== test session starts ==============================
collected 3 items

tests/test_api.py::test_app_won PASSED                                    [ 33%]
tests/test_api.py::test_app_lost PASSED                                   [ 66%]
tests/test_api.py::test_app_failure PASSED                                [100%]

=============================== 3 passed in 0.04s ===============================
```

### Front end

The frontend is implemented using Vue.js and Vuetify (a Material Design component
framework for Vue.js).
The HTTP requests to the server are performed with `axios`: an HTTP client for the browser.

**Requirements:**
- nodejs 12.7
- npm 6.10.3

It was tested with these versions. It might work with different versions.

The front end may not require `npm`/`nodejs` to run. See below.

Install the requirements

```sh
cd GuessingGame/frontend
npm install
```

To test the development environment:

```sh
npm run serve
```

Go to: http://localhost:8080/

Note the back end should be running in development.
There is proxy route in the `frontend/vue.config.js`. All the requests starting
with `/api` are routed to `http://localhost:5000`.

To build the production minimized javascript type:

```sh
npm run build
```

This creates the minimized files in: `frontend/dist`.

**NO NPM:**

Note that this folder is shipped!! `npm`/`nodejs` is not necessary.

In the `frontend` type:
```sh
python server.py
```

This simple webserver will serve the `dist` directory and will forward the
`/api` requests to the production server `localhost:8000` (this can be changed
at the top of the python file). The back end server must be therefore running in
production,

In a real production environment this would be done by for example `nginx`.
