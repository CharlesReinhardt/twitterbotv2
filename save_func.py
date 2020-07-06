# functions for saving current GonRain status into a local file

import requests
from bs4 import BeautifulSoup

def pull_weather(url):
	r = requests.get(url)

	soup = BeautifulSoup(r.content, 'html.parser')
	results = soup.find_all(attrs={'data-testid':'PrecipSection'})

	return (results)

def find_percent(s):
	loc1 = s.find('PercentageValue') + len('PercentageValue">')
	loc2 = s.find('%')
	percent = int(s[loc1:loc2])

	return(percent)

def is_greater(a, b):
	if a > b:
		return a
	else:
		return b

def rain_status(url):
	results = pull_weather(url)
	p1 = find_percent(str(results[0]))
	p2 = find_percent(str(results[1]))

	percent = is_greater(p1, p2)

	if percent >= 0 and percent <= 33:
		return ((0, 'It is not gon\' rain.'))
	elif percent > 33 and percent <= 66:
		return ((1, 'It is maybe gon\' rain.'))
	else:
		return ((2, 'It gon\' rain.'))

def save():
	url = 'https://weather.com/weather/tenday/l/Minneapolis+MN?canonicalCityId=c41f9794b3d2e73e76735276a2b073711dc220e4944a75a2ab0f9b91e91472d0'

	basedir = 'root'
	filename = 'today_status.txt'
	file = basedir + filename

	f = open(file, 'w')
	text = str(rain_status(url))
	f.write(text)
	f.close()

	print('status saved')

# Main Program #














