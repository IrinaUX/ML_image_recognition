# import necessary libraries
from flask import Flask, render_template, request, redirect, url_for
from keras.models import load_model

# create instance of Flask app
app = Flask(__name__)

# Set variables
model = load_model('saved_models/keras_cifar10_trained_model.h5')

# create route that renders index.html template
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        uploaded_file = request.files['uploadFile']
        if uploaded_file.filename != '':
            uploaded_file.save(uploaded_file.filename)
        return redirect(url_for('file_upload_form.html'))
    return render_template('file_upload_form.html')


if __name__ == "__main__":
    app.run(debug=True)
