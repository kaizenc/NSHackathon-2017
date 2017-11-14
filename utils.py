import requests
import json
from random import *
from vars import *


def get_purchases(account_id): #returns array of all details
	url = 'http://api.reimaginebanking.com/accounts/{}/purchases?key={}'.format(account_id,apiKey)
	purchases = requests.get(url).json()
	result = []
	for i in purchases:
		result.append(purchase_details(i["_id"]))
	result.sort(key=lambda x: (x[0], x[1]))
	return result

def sum_of_purchases(purchases):
	result = 0
	for i in purchases:
		result+=i[3]
	return result



def purchase_details(purchaseId):
	url = 'http://api.reimaginebanking.com/purchases/{}?key={}'.format(purchaseId,apiKey)
	purchase = requests.get(url).json()
	url2 = 'http://api.reimaginebanking.com/merchants/{}?key={}'.format(purchase['merchant_id'],apiKey)
	merchant = requests.get(url2).json()
	return [merchant['category'][0], purchase["purchase_date"], merchant['name'], purchase["amount"]]


def get_balance(account_id):
	url = 'http://api.reimaginebanking.com/accounts/{}?key={}'.format(account_id,apiKey)
	return requests.get(url).json()["balance"]

def populate(account_id):
	url = 'http://api.reimaginebanking.com/accounts/{}/purchases?key={}'.format(account_id,apiKey)

	merchants = [uber, chipotle, zara]
	for i in range(5):
		payload = {
		  "merchant_id": sample(merchants, 1)[0],
		  "medium": "balance",
		  "purchase_date": "2017-"+str(i+5)+"-"+str(randint(1, 28)),
		  "amount": randint(1, 25)*5,
		  "description": "description"
		}
		purchases = requests.post(url, data=json.dumps(payload), headers={'content-type':'application/json'})

def trenderize(all_purchases, category):
	data = [category, 0, 0, 0, 0, 0, 0, 0]
	for i in all_purchases:
		if(i[0] == category):
			month = int(i[1].split('-')[1])
			data[month-4] += i[3]
	return data