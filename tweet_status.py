# A program that tweets the GonRain status (from saved status file) when run

from datetime import date
import tweepy

def today():
	today = str(date.today())

	year = today[0:4]
	month = today[5:7]
	day = today[8:]

	return (month, day, year)

def date_format(month, day, year):
	d = months[month] + ' ' + day + ', ' + year

	return (d)

months = {
	'01' : 'January',
	'02' : 'February',
	'03' : 'March',
	'04' : 'April',
	'05' : 'May',
	'06' : 'June', 
	'07' : 'July', 
	'08' : 'August', 
	'09' : 'September', 
	'10' : 'October', 
	'11' : 'November', 
	'12' : 'December'
}

# Main Program #

# initialize twitter APIs

API_key = 'Cwwnr3TQMob04QJzUwo5reHNo'
API_secret_key = '9SUOksNEMwOMrlSc3fSEpQ6i2RrkVUs2IzppSxuYMjNQ2eVkv4'
access_token = '1268952631873060866-yzgpQ9d0lBEUIisKU6p7Pik8dxzQbN'
access_token_secret = 'hi9znx2N3v04uaEeA6Wcba1Riduaia1pFmXKNRqvA6hTv'

auth = tweepy.OAuthHandler(API_key, API_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# find and format date

today = today()
date = date_format(today[0], today[1], today[2])

# grab GonRain status from file

basedir = 'root'
filename = 'today_status.txt'
file = basedir + filename

f = open(file, 'r')
text = f.read()

loc1 = text.find('"') + 1 
loc2 = text.rfind('"')

status = text[loc1:loc2]

# build and tweet text

text = date + ': ' + status
print(text)
api.update_status(text)
