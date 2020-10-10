from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from keras.models import load_model
import pymongo

# from secret import username, password

app = Flask(__name__)

# Load the model
from keras.models import load_model
model = load_model('mnist.h5')
model = 

@app.route('/')
def hello_world():
    name = "project 3 - machine learning"
    return name


if __name__ == "__main__":
    app.run(debug=True)
