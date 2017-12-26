import requests
import datetime
import time
from geopy.geocoders import Nominatim


class Weather():
    def __init__(self, location, wakeUpTime):
        geolocator = Nominatim()
        geoLocation = geolocator.geocode(location)
        self.lat = str(geoLocation.latitude)
        self.lng = str(geoLocation.longitude)
        self.wakeUpTime = wakeUpTime
        self.key = "49e63ce753b5635f6c83a842fcc72c83"
        self.URL = "https://api.darksky.net/forecast/"

    def makeRequest(self):
        timeV = str(int(time.mktime(datetime.datetime.strptime(self.wakeUpTime, '%Y-%m-%d %H:%M').timetuple())))
        uri = self.URL + self.key + "/" + self.lat + "," + self.lng + "," + timeV + "?exclude=alerts,flags?lang=en"
        r = requests.get(uri)
        parsed_json = r.json()
        return parsed_json['currently']['apparentTemperature']




