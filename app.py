from flask import Flask
from our_functions.coordinates import get_coordinates


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"




# set FLASK_APP=hello
# set FLASK_ENV=development
