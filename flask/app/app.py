from flask import Flask
app = Flask(__name__)

from flask import render_template
import geojson
import json


@app.route('/')
def index():
    with open('data/layer_1.geojson', 'r') as file:  
        layer_1 = geojson.load(file)
        
    layer_1 = json.dumps({
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {
                    "scalerank": 8,
                    "type": "mid",
                    "name": "Shahid Ashrafi Esfahani",
                    "abbrev": "KSH",
                    "location": "runway",
                    "gps_code": "OICC",
                    "iata_code": "KSH",
                    "wikipedia": "http://en.wikipedia.org/wiki/Shahid_Ashrafi_Esfahani_Airport",
                    "natlscale": 10,
                    "featureclass": "Airport"
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        5,
                        52
                    ]
                }
            }
        ]
    }, indent=10)
    return render_template('index.html', layer_1=layer_1)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)