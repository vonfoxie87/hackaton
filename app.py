from flask import Flask, render_template, request, redirect, url_for
import os
from os.path import join, dirname, realpath
from our_functions.coordinates import get_coordinates
import folium


app = Flask(__name__)


UPLOAD_FOLDER = 'data'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER


@app.route('/upload')
def index():
     # Set The upload HTML template '\templates\index.html'
    return render_template('upload.html')


# Get the uploaded files
@app.route("/upload", methods=['POST'])
def uploadFiles():
    # get the uploaded file
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        # set the file path
        uploaded_file.save(file_path)
        # save the file
    return redirect(url_for('index'))


@app.route("/")
def hello_world():
    coordinaten = get_coordinates()
    middle = (len(coordinaten))
    middle = int(middle / 2)
    start_coords = coordinaten[middle]
    folium_map = folium.Map(location=start_coords, zoom_start=17)

    folium.Marker(
        location=coordinaten[0],
        popup="Start",
        icon=folium.Icon(color="green"),
    ).add_to(folium_map)


    folium.Marker(
        location=coordinaten[-1],
        popup="Eind",
        icon=folium.Icon(color="red"),
    ).add_to(folium_map)

    folium.PolyLine(
        locations=coordinaten,
        color="red",
        weight=12.5,
        opacity=1
    ).add_to(folium_map)
    return folium_map._repr_html_()

# set FLASK_APP=app
# set FLASK_ENV=development
# flask run
