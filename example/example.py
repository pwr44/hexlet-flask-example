from flask import Flask, request, render_template, make_response, jsonify

from data import generate_companies

companies = generate_companies(100)


app = Flask(__name__)


@app.route("/")
def hello_world():
    # создаем объект response
    response = make_response("Hello, World!")
    # Устанавливаем заголовок
    response.headers["X-MyHeader"] = "Thats my header!"
    # Меняем тип ответа
    response.mimetype = "text/plain"
    # Задаем статус
    response.status_code = 201
    # Устанавливаем cookie
    response.set_cookie("super-cookie", "42")
    return response

@app.route('/companies')
def get_companies():
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('per', 5, type=int)
    offset = (page - 1) * limit
    slice_of_companies = companies[offset:page * limit]
    return jsonify(slice_of_companies)


@app.route("/json/")
def json():
    return {"json": 42}  # Возвращает тип application/json


@app.route("/html/")
def html():
    return "<h1>Hello, world!</h1>"  # Возвращает тип text/html


@app.errorhandler(404)
def not_found(error):
    print(request.headers)
    return "Oops!", 404


# @app.route("/not_found/")
# def not_found():
#     return "Oops!", 404
