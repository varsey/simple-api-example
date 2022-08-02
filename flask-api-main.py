from flask import Flask, jsonify, request

from data.DataManipulator import DataManipulator as DM

app = Flask(__name__)


@app.route("/")
def route_hello_world():
    return "Hello, World."


@app.route("/blogs")
def route_all_blogs():
    return jsonify(dm.all_blogs())


@app.route("/blogs/<id>", methods=["GET"])
def route_get_blog(id: str):
    return jsonify(dm.get_blog(int(id)))


@app.route("/blogs/<id>", methods=["POST"])
def route_update_blog(id: str):
    data = request.get_json()
    return jsonify(dm.update_blog(int(id), data))


@app.route("/authors")
def route_all_authors():
    return jsonify(dm.all_authors())


@app.route("/authors/<id>")
def route_get_author(id: str):
    return jsonify(dm.get_author(int(id)))


if __name__ == "__main__":
    dm = DM()
    app.run(debug=True, host='0.0.0.0', port=5000)
