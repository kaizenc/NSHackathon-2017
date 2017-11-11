import requests
import json
from random import *

apiKey = '3a64a806ffb3ed0a94f771b9ae41a852'
customerId = '5a0677d5b390353c953a251f'
credit_card_id = '5a067873b390353c953a2520'
checking_id = '5a0678e5b390353c953a2521'
savings_id = '5a06798bb390353c953a2524'
uber = '5a06b6d2b390353c953a258b'
chipotle = '5a06b8f5b390353c953a2594'
zara = '5a06b938b390353c953a2596'


def get_purchases(account_id): #returns array of all details
	url = 'http://api.reimaginebanking.com/accounts/{}/purchases?key={}'.format(account_id,apiKey)
	purchases = requests.get(url).json()
	result = []
	for i in purchases:
		result.append(purchase_details(i["_id"]))
	result.sort(key=lambda x: (x[0], x[1]))
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
	data = [0, 0, 0, 0, 0, 0, 0]
	for i in all_purchases:
		if(i[0] == category):
			month = int(i[1].split('-')[1])
			data[month-5] += i[3]
	return data