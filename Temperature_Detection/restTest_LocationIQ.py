__author__ = 'AAK'

import requests
from urllib.request import urlopen
import json


def get_lat_long(place):

    '''
    Function to get the GPS coordinated of the place entered by the user.
    :param place: place
    :return:    lat,long
    '''

    api_key = '*******' #Enter the API KEY
    place = place.replace(" ","+")
    url = 'https://us1.locationiq.com/v1/search.php?key='+api_key+'&q='+place+'&format=json'
    obj_json = urlopen(url)
    input_json = json.load(obj_json)
    # print(input_json)
    lat = input_json[0]['lat']
    long = input_json[0]['lon']
    print('Coodrinates = {} , {}'.format(lat, long))
    return lat,long


