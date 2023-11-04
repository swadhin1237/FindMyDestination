from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import geocoder
from geopy.geocoders import Nominatim
from geopy.point import Point
import folium
from flask_restful import Api, Resource, reqparse
import random
import json
from .model import result

data=[]
source=""
destination=""


app = Flask(__name__)
api = Api(app)

def getImage(location_name):
    pass

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/search', methods=['GET','POST'])
def search():
    if request.method == 'POST':
        global source
        source = request.form['source']
        global destination
        destination = request.form['destination']
        tag=request.form['tag']
        global data
        data=result(destination,tag)
        return render_template('output.html', locations=data)
    return render_template('search.html')


@app.route('/output')
def output():
    global data
    print(data)
    return render_template('output.html',locations=data)

@app.route('/map/<idx>')
def map(idx):
    x=data[0]['Coordinates']['Latitude']
    y=data[0]['Coordinates']['Longitude']
    dest=[x,y]
    print(dest)

    map = folium.Map(location=dest, zoom_start=6)

    loc = Nominatim(user_agent="GetLoc")

    getLoc = loc.geocode(source)
    print(getLoc.address)

    addr = [getLoc.latitude, getLoc.longitude]

    folium.Marker(addr, popup='My Location').add_to(map)
    folium.Marker(dest, popup='Destination').add_to(map)
    map.save('templates/map.html')
    return render_template('map.html')

@app.route('/search/<idx>')
def get_image_info(idx):
    # Simulate retrieving image information (replace with your logic)
    return "yay"
if __name__ == "__main__":
    app.run(debug=True)