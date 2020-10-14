from flask import Flask, render_template, redirect, request, jsonify
from predict import predict_new 
import pandas as pd
import numpy as np
import os
import sys
import gevent 

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

from helperfunctions import b64_PIL, num_b64
from flask_socketio import SocketIO, emit, join_room, leave_room

# Create an instance of Flask
app = Flask(__name__)

# Load the model
model = load_model('saved_models/keras_cifar10_trained_model.h5')

# initiate RMSprop optimizer
opt = keras.optimizers.RMSprop(learning_rate=0.0001, decay=1e-6)

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

# Define the 10 classes into an array
class_names = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

# Resize the image before passing to the model
image_size = (32, 32)

# Select the image file
filepath = "images/horse.jpeg"

print("---------------> FLASK < --------------")
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print("IMAGE LOADED")
        img = image.load_img(filepath, target_size=image_size)
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        print("IMAGE PREPROCESSED")
    
        # request.result(data) MISSING THIS PART

        # print(request.files("file"))
        predictions = model.predict(x)  
        print(f'PREDICTED:, {predictions}')
        img = np.reshape(img,[1,32,32,3])
        print(f'RESHAPED PREDICTED IMAGE: {img}')
        classes = np.argmax(model.predict(img), axis = 1)
        names = [class_names[i] for i in classes]
        name = names[0]
        # json_name = jsonify(name)
        print(f"-------------> NAME {name}")
    return render_template('index.html', message = name)

if __name__ == "__main__":
    app.run(debug=True)
