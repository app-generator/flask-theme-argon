from argon_app import app
from flask_minify import Minify

DEBUG  = app.config['DEBUG']

if not DEBUG:
    Minify(app=app, html=True, js=False, cssless=False)

if __name__ == "__main__":
    app.run()

