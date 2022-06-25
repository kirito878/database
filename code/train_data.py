from hashlib import sha1
import hmac
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime
import base64
import requests
from pprint import pprint

app_id = 'da1d9183c40a448f97dee657149d89ad'
app_key = 'N3tt25MgpC8rs8jp05HuyXop_yU'


class Auth():

    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key

    def get_auth_header(self):
        xdate = format_date_time(mktime(datetime.now().timetuple()))
        hashed = hmac.new(self.app_key.encode('utf8'), ('x-date: ' + xdate).encode('utf8'), sha1)
        signature = base64.b64encode(hashed.digest()).decode()

        authorization = 'hmac username="' + self.app_id + '", ' + \
                        'algorithm="hmac-sha1", ' + \
                        'headers="x-date", ' + \
                        'signature="' + signature + '"'
        return {
            'Authorization': authorization,
            'x-date': format_date_time(mktime(datetime.now().timetuple())),
            'Accept-Encoding': 'gzip'
        }


def request(url):
    a = Auth(app_id, app_key)
    response = requests.get(url, headers=a.get_auth_header())
    result = response.json()
    return result

def station_data():
    result = request('https://ptx.transportdata.tw/MOTC/v2/Rail/THSR/Station?%24top=100&%24format=JSON')
    return result

def fares():
    result = request('https://ptx.transportdata.tw/MOTC/v2/Rail/THSR/ODFare?%24format=JSON')
    return result

def timetable():
    url = "https://ptx.transportdata.tw/MOTC/v2/Rail/THSR/GeneralTimetable?%24format=JSON"
    result = request(url)
    return result

def seat(day):
    url = f"https://ptx.transportdata.tw/MOTC/v2/Rail/THSR/AvailableSeatStatus/Train/Leg/TrainDate/{day}?%24format=JSON"
    result = request(url)
    return result



