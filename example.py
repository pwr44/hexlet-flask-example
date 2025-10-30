from flask import Flask, request


app = Flask(__name__)


@app.get("/")
def hello_get():
    print(request.headers)
    return "Hello, GET!"


@app.post("/")
def hello_post():
    return "Hello, POST!"

