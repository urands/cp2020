from flask import Flask
from datasets import load, load_buildings, load_invest
import os

app = Flask(__name__)

app.url_map.strict_slashes = False
_dir = os.path.dirname(os.path.abspath(__file__))
app.template_folder = os.path.join(_dir, "templates")
app.static_folder = os.path.join(_dir, "static")
app.config['UPLOAD_FOLDER'] = os.path.join(_dir, "upload")


power = load()
invest = load_invest()
apart = load_buildings()