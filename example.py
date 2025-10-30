from flask import Flask


app = Flask(__name__)


@app.get("/")
def hello_get():
    return "Hello, GET!"


@app.post("/")
def hello_post():
    return "Hello, POST!"

