__author__ = 'AAK'

import requests
from urllib.request import urlopen
import json

def get_temperature(latitude,longitude):

    '''
    Function to get the temperature of the place entered by the user.
    :param latitude:    latitude
    :param longitude:   longitude
    :return:    temp
    '''

    api_key = '******'  #Enter the API KEY
    url = 'https://api.breezometer.com/weather/v1/current-conditions?lat='+latitude+'&lon='+longitude+'&key=api_key'
    obj_json = urlopen(url)
    input_json = json.load(obj_json)
    # print(input_json)
    temp = list(input_json['data']['temperature'].values())
    return '{} degree Celsius'.format(temp[0], temp[1])
