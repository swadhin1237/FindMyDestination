from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import geocoder
from geopy.geocoders import Nominatim
from geopy.point import Point
import folium
from flask_restful import Api, Resource, reqparse
import random
import json
from .model import result
import requests

data=[]
source=""
destination=""

with open('data.json', 'r') as json_file:
    data_dict = json.load(json_file)

with open('data2.json', 'r') as json_file:
    data2 = json.load(json_file)


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
    # x=data[0]['Coordinates']['Latitude']
    # y=data[0]['Coordinates']['Longitude']
    x=data_dict['Temples'][0]['Coordinates']['Latitude']
    y=data_dict['Temples'][0]['Coordinates']['Longitude']
    dest=[x,y]
    print(dest)

    map = folium.Map(location=dest, zoom_start=6)

    loc = Nominatim(user_agent="GetLoc")

    source="Kolkata"
    getLoc = loc.geocode(source)
    print(getLoc.address)

    addr = [getLoc.latitude, getLoc.longitude]

    folium.Marker(addr, popup='My Location').add_to(map)
    # folium.Marker(dest, popup='Destination').add_to(map)
    

    map.save('templates/map.html')
    

    return render_template('map.html')

@app.route('/place/<idx>')
def place(idx):
    # x=data_dict['Temples'][0]['Coordinates']['Latitude']
    # y=data_dict['Temples'][0]['Coordinates']['Longitude']
    # dest=[x,y]
    # print(dest)
    # loc = Nominatim(user_agent="GetLoc")

    # source="Kolkata"
    # getLoc = loc.geocode(source)
    # print(getLoc.address)

    # addr = [getLoc.latitude, getLoc.longitude]

    # url = "https://sky-scrapper.p.rapidapi.com/api/v1/flights/getNearByAirports"

    # querystring1 = {"lat":f"{addr[0]}","lng":f"{addr[1]}"}

    # headers = {
	#     "X-RapidAPI-Key": "dfac622ff3msh5650dd6f3de63e6p1185eejsna79c050b7dc7",
	#     "X-RapidAPI-Host": "sky-scrapper.p.rapidapi.com"
    # }

    # response1 =  requests.get(url, headers=headers, params=querystring1)
    # print(response1)
    # querystring2 = {"lat":f"{dest[0]}","lng":f"{dest[1]}"}

    # response2 = requests.get(url, headers=headers, params=querystring2)  
    # print(response2)

    # id1=response1.json()['data']['current']['skyId']
    # id2=response2.json()['data']['current']['skyId']
    # ent1=response1.json()['data']['current']['entityId']
    # ent2=response2.json()['data']['current']['entityId']

    # print(id1,id2)

    # querystring = {"originSkyId":f"{id1}","destinationSkyId":f"{id2}","originEntityId":"27544008","destinationEntityId":"27537542","date":"2024-02-20","adults":"1","currency":"INR","market":"en-IN","countryCode":"IN"} 

    return render_template('place.html')

@app.route('/search/<idx>')
def get_image_info(idx):
    # Simulate retrieving image information (replace with your logic)
    return "yay"
if __name__ == "__main__":
    app.run(debug=True)