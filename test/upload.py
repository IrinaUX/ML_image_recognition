from flask import Flask, render_template, request, redirect, url_for
from keras.models import load_model

app = Flask(__name__)

@app.route('/')
def upload():
    return render_template("file_upload_form.html")


@app.route('/success', methods = ['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        return render_template("success.html", name = f/filename)

if __name__=='__main__':
    app.run(debug = True)