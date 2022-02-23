from flask import Flask, render_template
from our_functions.coordinates import get_coordinates
import folium




app = Flask(__name__)

@app.route("/")
def hello_world():
    test = get_coordinates()
    print(test)

    start_coords = (46.9540700, 142.7360300)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    return folium_map._repr_html_()




# set FLASK_APP=hello
# set FLASK_ENV=development
