from flask import Flask

plant_app = Flask(__name__)

from plant_app import views
from plant_app import admin_views
