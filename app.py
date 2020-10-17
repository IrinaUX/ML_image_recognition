#Dependencies 
import os
import sys
from flask import Flask, redirect, request, render_template,jsonify
from process_predict import predict_new, base64_to_pil
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # #Main page
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # #Get the image from post request
        image_new = base64_to_pil(request.json)

        # Make prediction and return result
        result = predict_new(image_new)
        return jsonify(result=result)
    return None


@app.route('/draw.html', methods=['GET', 'POST'])
def draw():
    return render_template('draw.html')

if __name__ == '__main__':
    # Serve the app with gevent
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()
 
   
 
