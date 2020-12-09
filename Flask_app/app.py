import os
import pandas as pd 
import numpy as np 
import flask
import pickle
from flask import Flask, render_template, redirect, url_for, request
from flask_cors import CORS

# Create an instance of Flask
app = Flask(__name__)
CORS(app)

app.config["DEBUG"] = True

# import dataset and define features as a variable
dataset = pd.read_csv('../Datasets/insurance.csv')
X = dataset.iloc[:, :-1].values

# OnehotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
# Create object of the column transformer class
# [0] is the index of column to apply OneHotEncoding
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [1,4,5])], remainder='passthrough')
X = np.array(ct.fit_transform(X))
model_file = pd.read_pickle("../Jupyter Notebooks/model.pkl")

# Landing page
@app.route("/")
def home():
    return flask.render_template("index.html")

# Model runs using passed in variables and outputs the prediction
def predict_model(age, gender, bmi, children, smoker, region):
    user_inputs = []
    user_inputs.append(age)
    user_inputs.append(gender)
    user_inputs.append(bmi)
    user_inputs.append(children)
    user_inputs.append(smoker)
    user_inputs.append(region)
    print(user_inputs)
    predicted_value = model_file.predict(ct.transform([user_inputs]))
    return(predicted_value)

# Route that will receive input form data
@app.route("/", methods=["GET", "POST"])
def calc_charges():
    if request.method == "POST":
        predict_list = request.form.to_dict()
        predict_list = list(predict_list.values())
        # print(predict_list)
        age = request.form["Age"]
        no_children = request.form["no. child"]
        bmi = request.form["bmi"]
        gender = request.form["gender"]
        smoker = request.form["smoker"]
        region = request.form["region"]
        prediction = predict_model(age, gender, bmi, no_children, smoker, region)

        # Redirect back to home page with prediction to display
        return render_template("index.html",prediction=round(prediction[0],2))


if __name__ == "__main__":
    app.run(debug=True)