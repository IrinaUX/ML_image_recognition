# import necessary libraries
from flask import Flask, render_template
from keras.models import load_model

# create instance of Flask app
app = Flask(__name__)

# Set variables
model = load_model('saved_models/keras_cifar10_trained_model.h5')

# create route that renders index.html template
@app.route("/")
def echo():

    return render_template("index.html", model=model)


if __name__ == "__main__":
    app.run(debug=True)
