
from app import create_app
from app.config import ProductionConfig

'''

Run this as:
gunicorn -w <number of workers> --bind <IP>:<port> run_prod:app

E.g.:
gunicorn -w 2 --bind localhost:8000 run_prod:app

'''


app = create_app(ProductionConfig)
