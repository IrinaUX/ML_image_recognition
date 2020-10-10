from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from keras.models import load_model
import pymongo

# from secret import username, password

app = Flask(__name__)

# Load the model
from keras.models import load_model

model = load_model('saved_models/keras_cifar10_trained_model.h5')

@app.route('/')
def hello_world():
    name = "project 3, group 6 - machine learning"

    
    return name

@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    return render_template("upload_image.html")


if __name__ == "__main__":
    app.run(debug=True)
