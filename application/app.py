from flask import Flask, render_template, redirect, request
from predict import predict_new 

# Create an instance of Flask
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
      if request.method == "POST":
          #call predict function to label new image
          new_image = predict_new(new_image)
          return render_template('index.html', message = new_image)

if __name__ == "__main__":
    app.run()