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


def getImage(location_name):
    pass
app = Flask(__name__)


api = Api(app)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/search', methods=['GET','POST'])
def search():
    if request.method == 'POST':
        source = request.form['source']
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

@app.route('/search/<idx>')
def get_image_info(idx):
    # Simulate retrieving image information (replace with your logic)
    return "yay"
if __name__ == "__main__":
    app.run(debug=True)