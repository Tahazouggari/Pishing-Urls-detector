# app.py

from flask import Flask, render_template, request
from src.utils import predict_url

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            result = predict_url(url)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
