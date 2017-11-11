from flask import Flask, render_template, url_for

import requests
import json

import utils


app = Flask(__name__)

@app.route("/")
def main():
	print(utils.trenderize(utils.get_purchases(utils.credit_card_id),"Food"))
	return render_template("page.html", purchases=utils.get_purchases(utils.credit_card_id), balance=utils.get_balance(utils.credit_card_id))

@app.route("/trends")
def trends():
	return render_template("page2.html", balance=utils.get_balance(utils.credit_card_id), 
		food_data=utils.trenderize(utils.get_purchases(utils.credit_card_id),"Food"),
		clothes_data=utils.trenderize(utils.get_purchases(utils.credit_card_id),"Clothes"))

if __name__ == "__main__":
  app.debug = True
  app.run(host="0.0.0.0", port=8000)