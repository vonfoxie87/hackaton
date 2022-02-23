from flask import Flask, render_template
from our_functions.coordinates import get_coordinates
import folium


app = Flask(__name__)

@app.route("/")
def hello_world():
    coordinaten = get_coordinates()

    start_coords = (51.9066667, 4.188611111111111)
    folium_map = folium.Map(location=start_coords, zoom_start=17)


    folium.Marker(
        location=(51.9066667, 4.188611111111111),
        popup="Start",
        icon=folium.Icon(color="green"),
    ).add_to(folium_map)
    folium_map

    folium.PolyLine(
        locations=[(51.9066667,4.188611111111111),(51.9044444,4.184166666666667)],
        color="red",
        weight=2.5,
        opacity=1
    ).add_to(folium_map)
    folium_map

    return folium_map._repr_html_()



# set FLASK_APP=hello
# set FLASK_ENV=development
