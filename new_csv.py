from flask import Flask, json, request, redirect, render_template, jsonify
import csv, pandas
from pandas.core.indexes.datetimes import date_range

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("SPA.html")


@app.route("/login", methods=['POST',"GET"])
def login():
    if request.method == "POST":
        name = request.get_json('uname')
        password = request.get_json('pword')
        filename = 'newfile.csv'
        # data = pandas.read_csv(filename)
        return "Logged IN"


@app.route("/inputs", methods=["POST"])
def input():
    if request.method == 'POST':
        name = request.get_json("name")
        comment = request.get_json("comments")
        fieldnames = ['name', 'comment']
        with open("newfile.csv", 'a') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({"name":name, 'comment':comment})
        return jsonify({"name":name, "comments":comment})


if __name__ == '__main__':
    app.run(debug=True)
