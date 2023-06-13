# -- coding: utf-8
import requests
from os import path
from json import load

path_TOKEN = path.join('C:\\Users\\1\\Desktop\\tokens\\tokens.json')
with open(path_TOKEN, 'r') as tokens:
    TOKEN = load(tokens)['token_for_weather']


LINK = 'http://api.openweathermap.org/data/2.5/weather?id=${cityId}&lang=ru&units=metric&APPID={TOKEN}'
