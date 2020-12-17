__author__ = 'AAK'

from zeep import Client


def convert_temperature(temp):

    '''
    Function to convert the obtained temperature of the place in Celsius to temperature in Fahrenheit
    :param temp:  temp
    :return:    converted_temp
    '''

    client = Client(wsdl='******') #Enter link
    converted_temp = client.service.CelsiusToFahrenheit(temp)
    print(converted_temp)
    return converted_temp
