import mh_z19
import time
import schedule
import json
import requests

CheckUrl = 'NET connech check url'
Url = "API LINK"


def job():
	if not CheckNetWork():
		print("NETWORK Failed")
	else:
		sendData()
		
	
def getTemp():
	temp = mh_z19.read()
	return temp['co2']

def sendData():
	out = getTemp()
	requests.get(Url+ str(out))

def CheckNetWork():
	try:
		requests.head(CheckUrl)
		return True
	except requests.ConnectionError as ex:
		return False
		
	
	
job()
schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)