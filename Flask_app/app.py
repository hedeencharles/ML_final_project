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
def home():
    return flask.render_template("index.html")

def ValuePredictor(predict_list):
    to_predict = np.array(predict_list).reshape(1,6)
    loaded_model = pickle.load(open("model.pkl","rb"))
    calc_charges = loaded_model.predict(to_predict)
    return calc_charges[0]

# Route that will receive input form data
@app.route("/", methods=["GET", "POST"]) # need to figure this line out
def calc_charges():
    if request.method == "POST":
        predict_list = request.form.to_dict()
        predict_list = list(predict_list.values())
        # predict_list = list(map(float, to_predict_list))
        calc_charges = ValuePredictor(predict_list)
        prediction = float(calc_charges)


        # charges = Charges(
        #     age=request.form["age"],
        #     gender=request.form["gender"],
        #     bmi=request.form["bmi"],
        #     children=request.form["children"],
        #     smoker=request.form["smoker"],
        #     region=request.form["region"],
        # )

    # Redirect back to home page
    return redirect(url_for('home'), prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)