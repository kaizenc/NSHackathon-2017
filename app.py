from flask import Flask, render_template, url_for

import requests
import json

from utils import *


app = Flask(__name__)

@app.route("/")
def main():
	purchases = get_purchases(credit_card_id)+get_purchases(savings_id)
	purchases.sort(key=lambda x: (x[0], x[1]))
	return render_template("page.html", purchases=purchases, 
		balance=get_balance(credit_card_id),
		balance1=get_balance(checking_id),
		balance2=get_balance(savings_id))

@app.route("/trends")
def trends():
	all_purchases = get_purchases(credit_card_id)+get_purchases(savings_id)
	return render_template("page2.html", balance=get_balance(credit_card_id),
		balance1=get_balance(checking_id),
		balance2=get_balance(savings_id),
		food_data=trenderize(all_purchases,"Food"),
		clothes_data=trenderize(all_purchases,"Clothes"))

if __name__ == "__main__":
  app.debug = True
  app.run(host="0.0.0.0", port=8000)