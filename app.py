from flask import Flask, render_template, request, redirect, url_for, request
import os
from our_functions.coordinates import get_coordinates
from our_functions.zaken import create_zaak, get_all_zaken
import folium


app = Flask(__name__)


UPLOAD_FOLDER = 'data'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER


@app.route('/')
def index():
    if request.method == 'POST':
        create_zaak()
    zaken = get_all_zaken()
    return render_template('index.html', zaken=zaken)


@app.route('/map_folium')
def folium_map():
    return render_template('map_folium.html')


@app.route('/upload')
def upload():
    # Set The upload HTML template '\templates\index.html'
    return render_template('upload.html')


# Get the uploaded files
@app.route("/upload", methods=['POST'])
def uploadFiles():
    # get the uploaded file
    uploaded_file = request.files['file']

    if uploaded_file.filename != '':
        if uploaded_file.filename[-3:] == "csv" or uploaded_file.filename[-3:] == "CSV":
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
            # set the file path
            uploaded_file.save(file_path)
            # save the file
        else:
            print('error')
    return redirect(url_for('index'))


@app.route("/map")
def map():
    coordinaten = get_coordinates()
    middle = (len(coordinaten))
    middle = int(middle / 2)
    start_coords = coordinaten[middle]
    folium_map = folium.Map(
                            location=start_coords,
                            height='100%',
                            width='100%',
                            zoom_start=17)

    folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr='Esri',
        name='Esri Satellite',
        overlay=False,
        control=True
        ).add_to(folium_map)

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
        weight=10,
        opacity=1
    ).add_to(folium_map)
    folium_map.save('templates/map_folium.html')
    return render_template('map.html')
    #return folium_map._repr_html_()

# set FLASK_APP=app
# set FLASK_ENV=development
# flask run
