from flask import Flask, render_template, request, redirect, url_for
import os
from our_functions.coordinates import get_coordinates
from our_functions.zaken import create_zaak, create_zaak_table, get_all_zaken, create_zoekpatroon, get_zoekpatronen
import folium


app = Flask(__name__)


UPLOAD_FOLDER = 'data'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['POST', 'GET'])
def index():
    create_zaak_table()
    if request.method == 'POST':
        naam = request.form.get('naam_zaak')
        create_zaak(naam)
    zaken = get_all_zaken()
    return render_template('index.html', zaken=zaken)


@app.route('/zaak/<id>', methods=['POST', 'GET'])
def zaak(id):
    id = id
    create_zaak_table()
    if request.method == 'POST':
        id_zoek = request.form.get('id_zoekpatroon')
        naam = request.form.get('naam')
        naam_zoek = request.form.get('naam_zoekpatroon')
        datum_zoek = request.form.get('datum_zoekpatroon')
        file_zoek = request.form.get('file_zoekpatroon')
        uploaded_file = request.files['file_zoekpatroon']
        if uploaded_file.filename != '':
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
            file_zoek = uploaded_file.filename
            uploaded_file.save(file_path)
        create_zoekpatroon(id_zoek, naam, naam_zoek, datum_zoek, file_zoek)
    zoek_patroon = get_zoekpatronen(id)
    return render_template('zaak.html', zoek_patroon=zoek_patroon)


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
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        uploaded_file.save(file_path)

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
