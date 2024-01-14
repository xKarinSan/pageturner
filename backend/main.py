from flask import Flask, jsonify
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    data = {"message": "Hello, World!"}
    return jsonify(data)


@app.route("/hi")
def hi():
    data = {"message": "Hello!"}
    return jsonify(data)


@app.route("/user/<username>")
def show_user_profile(username):
    # show the user profile for that user
    # return f'User {escape(username)}'
    return jsonify({"username": username})


@app.route("/post/<int:post_id>")
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f"Post {post_id}"


@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    # show the subpath after /path/
    return f"Subpath {escape(subpath)}"
