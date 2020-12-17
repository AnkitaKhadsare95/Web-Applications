# Web Application to find current temperature of a desired location.

## Introduction

This web application takes as input a name of a place, it then returns the Global Positioning System (GPS) coordinates that is the Latitude and Longitude of the location entered by the user. These coordinates are further used to find the current temperature at this location in Celsius. Lastly, this temperature is converted to Fahrenheit and temperature in both the scales is displayed on the application to enhance user readability.

## This application invokes the following three Web Services

The list below shows the API Name, Link	and Service respectively.
1. LocationIQ - https://locationiq.com/docs (RESTful service)
2. Breezometer -https://docs.breezometer.com/api-documentation/weather-api/v1/#current-conditions (RESTful service)
3. TempConvert	https://www.w3schools.com/xml/tempconvert.asmx?wsdl (SOAP based service)

## Description of the Web Services used
1.	LocationIQ API– I used this API to get the GPS coordinates, that is the Latitude and Longitude values for the location entered by the user.
2.	Breezometer API – This API is used to find the current temperature details based on the GPS
coordinates. It will return the current temperature in Celsius for the location specified by the user.
3.	TempConvert API – I used this API to convert the temperature obtained in Celsius scale to temperature in Fahrenheit scale. Thus, it returns the temperature in Fahrenheit scale for the location specified by the user.

## More About the Application
* In order to develop this application, I have used Python programming language. I used Python 3 with a web application framework called Flask.
*	In order to invoke the RESTful services, I used the ‘requests’ library. With the help of this library, HTTP requests can be made in Python.
*	To invoke the SOAP based service with WSDL, I used the ‘zeep’ library. It inspects the code so that we can use the services and types in the document.
*	I have used HTML forms in order to get input from user and display output to the user.
*	I have also used the ‘json’ library to parse the information generated in json format.

## Instructions to run this application

In order to run this application, you need Python3 interpreter installed in your system. 
It should be accessible through command line. 
Check if your system meets all the requirements mentioned in the requirements.txt file.
Further, unzip the code, and run the application from the terminal by writing the following command:

python web_app.py 

 or 

python3 web_app.py

Run the command. Now, check the status of the application on your default browser.
To check the status of your application, type http://localhost:5000 in your browser.

Details about the application are mentioned in the Report.

**Note: You will require the Api-Key to invoke the RESTful services and the WSDL to invoke the SOAP Service.**

## Working of the application

**Step 1:**
On running the application, the first page of the application can be seen in Figure 1. User is required to enter the name of a place in the input field. The first page is the ‘homepage_name.html’ webpage created in the templates directory in flask.

![Figure 1](https://github.com/AnkitaKhadsare95/Web-Applications/blob/main/Temperature_Detection/images/Figure%201.png?raw=true)
 
**Step 2:**
Once the user enters a valid name of place as input, example- ‘Rochester’, he/she will have to click the Search button. On entering a place, the application screen will look as in Figure 2.

![Figure 2](https://github.com/AnkitaKhadsare95/Web-Applications/blob/main/Temperature_Detection/images/Figure%202.png?raw=true)
 
**Step 3:**
The output obtained on clicking the Search button is seen on the next page. Figure 3 shows this next webpage with the output. This output is obtained on sending the name of the place to the LocationIQ API using the POST method. This second page is the ‘WeatherDetails.html’ webpage created in the templates directory in flask.

![Figure 3](https://github.com/AnkitaKhadsare95/Web-Applications/blob/main/Temperature_Detection/images/Figure%203.png?raw=true)
 
**Step 4:**
* On clicking the ‘Get Temperature’ button the user is directed to a new webpage, that displays the temperature of the place entered by the user. The temperature in Celsius is obtained on passing the GPS coordinates to the Breezometer API.
* Further, the webpage also displays the temperature that is converted from Celsius to Fahrenheit scale. For this, the output temperature generated from using the Breezometer API (that is in Celsius) is passed to the operation ‘CelsiusToFahrenheit()’ on the SOAP based API TempConvert and the output obtained, that is temperature in Fahrenheit scale is displayed on the webpage.
* This third page is the ‘DisplayTemperature.html’ webpage created in the templates directory in flask.
* Figure 4 shows the output screen of the webpage.

![Figure 4](https://github.com/AnkitaKhadsare95/Web-Applications/blob/main/Temperature_Detection/images/Figure%204.png?raw=true)

**Step 5:**
All the images used for background purposes are downloaded from the internet. These images are stored in the ‘static’ directory in flask.
 
## Conclusion:
As the application finds the temperature of a location based on the GPS coordinates, hence it will always return an accurate value for the current temperature in that area. Also, as different countries use different metric scale for temperature calculation, this application is beneficial as it returns the current temperature in both Celsius and Fahrenheit scale. Thus, this application is very user-friendly.
