from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import geocoder
from geopy.geocoders import Nominatim
from geopy.point import Point
import folium
from flask_restful import Api, Resource, reqparse
import random
import json

# Read and parse the JSON file
with open('dataset.json', 'r') as json_file:
    data = json.load(json_file)


def loca():
    g=geocoder.ip("me")
    myAddr=g.latlng
    geolocator=Nominatim(user_agent="myGeocoder")
    loc=f'{myAddr[0]} , {myAddr[1]}'
    locname=geolocator.reverse(loc)
    print(locname.addr)
    return myAddr

def getImage(location_name):
    pass
app = Flask(__name__)


api = Api(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/location')
def location():
    addr=loca()
    return addr

@app.route('/search', methods=['GET','POST'])
def search():
    if request.method == 'POST':
        source = request.form['source']
        destination = request.form['destination']
        tag=request.form['tag']

        print(result)
        return render_template('search.html', result=result)

    return render_template('search.html')

@app.route('/map')
def map():
    addr=loca()
    map = folium.Map(location=addr, zoom_start=12)
    print(addr)
    folium.Marker(addr, popup='My Location').add_to(map)
    map.save('templates/map.html')
    return render_template('map.html')

@app.route('/output')
def output():
    return render_template('output.html',locations=data)

@app.route('/search/<idx>')
def get_image_info(idx):
    # Simulate retrieving image information (replace with your logic)
    return "yay"
if __name__ == "__main__":
    app.run(debug=True)
