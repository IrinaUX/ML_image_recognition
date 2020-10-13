# import necessary libraries
from flask import Flask, render_template, jsonify, request, redirect, url_for
from keras.models import load_model
import base64

# create instance of Flask app
app = Flask(__name__)

# Set variables
model = load_model('saved_models/keras_cifar10_trained_model.h5')

# create route that renders index.html template
@app.route('/', methods=['GET', 'POST'])
def index():
        
    if request.method == 'POST':
        uploaded_file = request.files['upload']
        if uploaded_file.filename != '':
            uploaded_file.save(uploaded_file.filename)
            print("***************************")
            print(uploaded_file.read())
            print("***************************")
    return render_template('index.html')

        


if __name__ == "__main__":
    app.run(debug=True)
