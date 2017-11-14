from flask import Flask, render_template, url_for

import requests
import json

from utils import *


app = Flask(__name__)

@app.route("/")
def main():
	all_purchases = get_purchases(savings_id)+get_purchases(checking_id)
	all_purchases.sort(key=lambda x: (x[0], x[1]))
	return render_template("page.html",all_purchases=all_purchases,
		balance1=get_balance(checking_id),
		balance2=get_balance(savings_id), 
		expenses=sum_of_purchases(all_purchases))

@app.route("/trends")
def trends():
	all_purchases = get_purchases(savings_id)+get_purchases(checking_id)
	data_ = [trenderize(all_purchases,"Food"),trenderize(all_purchases,"Clothes"),trenderize(all_purchases,"Transportation")]
	return render_template("page2.html",
		balance1=get_balance(checking_id),
		balance2=get_balance(savings_id),
		data = data_, 
		size = len(data_))

if __name__ == "__main__":
  app.debug = True
  app.run(host="0.0.0.0", port=8000)