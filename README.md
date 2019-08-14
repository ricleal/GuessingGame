# GuessingGame
Guessing Game Take-Home Problem


# Production

```
gunicorn -w <number of workers> --bind <IP>:<port> run_prod:app

# E.g.:
gunicorn -w 2 --bind 0.0.0.0:8000 run_prod:app
```
