from flask import Flask

app = Flask(__name__)

# @app.route("/")
# def index():
#     return "Site 3"

@app.route('/')
def index():
  return render_template('index.html')
