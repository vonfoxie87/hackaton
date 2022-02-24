from app import app, db
from app.models import Zaak, Zoeking
from flask import render_template, request, redirect, url_for, request
from our_functions.coordinates import get_coordinates
import folium
import os


@app.route('/', methods=['POST', 'GET'])
def index():
    message = ''
    if request.method == 'POST':
        naam = request.form.get('naam_zaak')
        q = Zaak(naam=naam)
        db.session.add(q)
        db.session.commit()
        message = "De zaak is opgeslagen"
    zaken = Zaak.query.all()
    return render_template('index.html', zaken=zaken, message=message)

@app.route('/zaak/<id>', methods=['POST', 'GET'])
def zaak(id):
    message = ''
    if request.method == 'POST':
        naam = request.form.get('naam_zoeking')
        q = Zoeking(naam=naam, zaak_id=id)
        db.session.add(q)
        db.session.commit()
        message = "De zoeking is opgeslagen"
    zaak = Zaak.query.filter_by(id=id).first()
    zoekingen = Zoeking.query.filter_by(zaak_id=id).all()
    return render_template('zaak.html', zaak=zaak, zoekingen=zoekingen, message=message)

@app.route('/zaak/<zaak>/zoeking/<id>')
def zoeking(zaak, id):
    zoeking = Zoeking.query.filter_by(id=id).first()
    return render_template('zoeking.html', zoeking=zoeking)

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
    folium_map.save('app/templates/map_folium.html')
    return render_template('map.html')
    #return folium_map._repr_html_()

# set FLASK_APP=app
# set FLASK_ENV=development
# flask run