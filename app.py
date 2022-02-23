from flask import Flask
from our_functions.coordinates import get_coordinates
import folium


app = Flask(__name__)

@app.route("/")
def hello_world():
    coordinaten = get_coordinates()
    middle = (len(coordinaten))
    middle = int(middle / 2)
    print(middle)
    start_coords = coordinaten[middle]
    folium_map = folium.Map(location=start_coords, zoom_start=17)

    folium.Marker(
        location=coordinaten[0],
        popup="Start",
        icon=folium.Icon(color="green"),
    ).add_to(folium_map)
    folium_map

    folium.Marker(
        location=coordinaten[-1],
        popup="Eind",
        icon=folium.Icon(color="red"),
    ).add_to(folium_map)
    folium_map


    folium.PolyLine(
        locations=coordinaten,
        color="red",
        weight=2.5,
        opacity=1
    ).add_to(folium_map)
    folium_map

    return folium_map._repr_html_()



# set FLASK_APP=app
# set FLASK_ENV=development
# flask run
