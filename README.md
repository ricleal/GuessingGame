# GuessingGame

Guessing Game Take-Home Problem

## 

I could do much better if time allowed...

For now I have flask serving everything. Flask has the possibility to have static directory
and I pointed the `dist` directory of the front end to there.
In a production environment I would never do this!!!


## Instalation


**Requirements:**
- Python 3.6
- PIP
- Python Virtual Environment (`virtualwnv`) is optional but recommended.


To deploy the app locally, first create a virtual environment and activate it(optional):

```sh
# virtualenv creation
virtualenv venv -p python3
# virtualenv activation
source venv/bin/activate
```

Install the requirements:
```
pip install -r requirements.txt
```

Create an `.env` file (file with the definition of environment variables). See `env.base` for a template.
If the file / environment variable does not exist, the default argument (the second) of `os.getenv` is used. See `app/config.py` for more details.

Fire up the app in development:
```
python run_dev.py
```
To test: http://localhost:5000/static/index.html

In production:
```
gunicorn -w <number of workers> --bind <IP>:<port> run_prod:app

# E.g.:
gunicorn -w 2 --bind 0.0.0.0:8000 run_prod:app
```
To test: https:// 0.0.0.0:8000/static/index.html



## Front end

Install `vue-cli`:
```
npm install -g @vue/cli
```

https://cli.vuejs.org/


Now there is build for development:
```
npm run serve
```
http://localhost:8080/?

or 

```
 npm run build
```

This creates the minimized files in: `frontend/guessing/dist`.

For production all links are prefixed with `/static`.
See: `frontend/guessing/vue.config.js` for the configuration.



## Backend

We can launch the server in dev:
```
python run_dev.py 
```




Or for production:


```
gunicorn -w <number of workers> --bind <IP>:<port> run_prod:app

# E.g.:
gunicorn -w 2 --bind 0.0.0.0:8000 run_prod:app
```

Go to : http://0.0.0.0:8000/static/index.html

# tests 

There are only tests for the backend. I did not have time for writting tests for the frontend.

Tests in the back end 