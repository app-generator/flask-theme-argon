import os

# import Flask 
from flask import Flask

from argon_app.config import Config

# Inject Flask magic
app = Flask(__name__)

# load Configuration
app.config.from_object( Config ) 


# Import routing to render the pages
from argon_app import views

