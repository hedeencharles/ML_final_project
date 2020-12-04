import os
import pandas as pd 
import numpy as np 
import flask
import pickle
from flask import Flask, render_template, redirect, url_for, request

# Create an instance of Flask
app = Flask(__name__)

# Landing page
@app.route("/")
def index():
    return flask.render_template("index.html")

# Route that will receive input form data
@app.route("/user/add", methods=["GET", "POST"]) # need to figure this line out
def calc_charges():
    if request.method == "POST":
        charges = Charges(
            age=request.form["age"],
            gender=request.form["gender"],
            bmi=request.form["bmi"],
            children=request.form["children"],
            smoker=request.form["smoker"],
            region=request.form["region"],
        )

    # Redirect back to home page
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)