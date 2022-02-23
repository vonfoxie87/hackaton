from flask import Flask, render_template
from our_functions.coordinates import get_coordinates


app = Flask(__name__)

@app.route("/")
def hello_world():
    test = get_coordinates()
    print(test)
    return render_template('index.html')




# set FLASK_APP=hello
# set FLASK_ENV=development
