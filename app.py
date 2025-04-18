# app.py
from flask import Flask           # import flask
app = Flask(__name__)             # create an app instance

@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return "Hello World!"         # which returns "hello world"

@app.route("/about")                   # at the end point /
def about():                      # call method hello
    return "<h2>Welcome my Flask App</h2>"         # which returns "hello world"

@app.route("/contact")                   # at the end point /
def kuchv():                      # call method hello
    return "<h2>My Contact page</h2>"         # which returns "hello world"

if __name__ == "__main__":        # on running python app.py
    app.run() 