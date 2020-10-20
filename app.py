import os
# import sys

# Flask
from flask import Flask, redirect, request, render_template, jsonify
# redirect, Response, url_for
# from werkzeug.utils import secure_filename
# from gevent.pywsgi import WSGIServer

# TensorFlow and tf.keras
# import tensorflow as tf
# from tensorflow import keras

from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

import re
import base64

import numpy as np

from PIL import Image
from io import BytesIO
# from process_predict import model_predict

def base64_to_pil(img_base64):
   
    image_data = re.sub('^data:image/.+;base64,', '', img_base64)
    pil_image = Image.open(BytesIO(base64.b64decode(image_data)))
    return pil_image

app = Flask(__name__)

print('Model loaded. Check http://127.0.0.1:5000/')


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

@app.route('/draw.html', methods=['GET', 'POST'])
def draw():
    return render_template('draw.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get the image from post request
        img = base64_to_pil(request.json)

        # Make prediction
        preds = model_predict(img)
        # print(preds, "ATTENTION")

        class_names = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

        # find the index of the class with maximum score
        pred = np.argmax(preds, axis=-1)
        result = class_names[pred[0]]
        print(result, pred,'TOKEN' )
       
        pred_proba = "{:.3f}".format(np.amax(preds))
        
        # Serialize the result, you can add additional fields
        return jsonify(result=result, probability=pred_proba)

    return None

# load model
# MODEL_PATH = 'saved_models/keras_cifar10_trained_model.h5'
MODEL_PATH = 'saved_models/Vgg13_model.h5'
model = load_model(MODEL_PATH)
print('local host started at port 5000')

# define global variables
class_names = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 
               'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

# define predict function with variables that changes for new input
def model_predict(image_new):
    img = image_new.resize((32, 32))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x, mode='tf')
    preds = model.predict(x)
    return preds


if __name__ == '__main__':
    app.run(threaded=True)
    # # Serve the app with gevent
    # http_server = WSGIServer(('0.0.0.0', 5000), app)
    # http_server.serve_forever()
    