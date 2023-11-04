from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import geocoder
import folium
from flask_restful import Api, Resource, reqparse
import random




def loca():
    g=geocoder.ip("me")
    myAddr=g.latlng
    return myAddr

app = Flask(__name__)


api = Api(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/location')
def location():
    addr=loca()
    return addr

app.run(debug=True)


