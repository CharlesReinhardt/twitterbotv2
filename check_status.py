# checks the current GonRain status against the previously saved GonRain status

import requests
from bs4 import BeautifulSoup
from datetime import date
import tweepy

import save_func as s
import update_func as u

# main program #

# grab saved status 

url = 'https://weather.com/weather/tenday/l/Minneapolis+MN?canonicalCityId=c41f9794b3d2e73e76735276a2b073711dc220e4944a75a2ab0f9b91e91472d0'

basedir = '/Users/charliereinhardt/Documents/Coding_Shenanigans/GonRainProject/twitterbotv2/'
filename = 'today_status.txt'
file = basedir + filename

f = open(file, 'r')
saved_status = int((f.read()[1]))

# find current status from weather data 

current_status = (s.rain_status(url)[0])

# compare current and saved status

if saved_status < current_status:
	# change saved status
	s.save()
	# tweet
	# u.update()
else: 
	print('status not different')
