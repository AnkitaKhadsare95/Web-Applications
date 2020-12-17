__author__ = 'AAK'

'''
CSCI-724: Web Services and Service Oriented Computing
Author: Ankita Anilkumar Khadsare [ak8932] 

Programming Assignment 1 : Web Application to find current temperature of a desired location.
'''

from flask import Flask, render_template, jsonify, request
from restTest_LocationIQ import get_lat_long
from restTest_Breezometer import get_temperature
from soapTest_Temperature import convert_temperature

web_app = Flask(__name__)


@web_app.route('/')
def get_place():
    return render_template('homepage_name.html')


@web_app.route('/WeatherDetails', methods=['POST', 'GET'])
def WeatherDetails():
    if request.method == 'POST':
        place1 = request.form['place']
        lat, long = get_lat_long(place1)
        return render_template("WeatherDetails.html", place=place1, lat=lat, long=long)


@web_app.route('/DisplayTemperature', methods=['POST', 'GET'])
def DisplayTemperature():
    if request.method == 'POST':
        place = request.form['place']
        lat, long = request.form['lat'], request.form['long']
        temp = get_temperature(lat, long)
        converted_temp = convert_temperature(temp.strip().split()[0])
    return render_template("DisplayTemperature.html", place= place, lat=lat, long=long, temp=temp, converted_temp=converted_temp)


if __name__ == "__main__":
    web_app.run()
