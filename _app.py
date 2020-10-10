from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from keras.models import load_model
import pymongo

# from secret import username, password

app = Flask(__name__)

# Load the model
from keras.models import load_model

model = load_model('saved_models/keras_cifar10_trained_model.h5')

text_to_render = "rendered from app.py"

# create route that renders index.html template
@app.route("/")
def echo():

    return render_template("index.html", text=text_to_render)

    
    return text


if __name__ == "__main__":
    app.run(debug=True)
