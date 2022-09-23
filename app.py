from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/")
# def index():
#     return "Site 3"

@app.route('/')
def index1():
  return render_template('index.html')
