from flask import Flask
from api import api

app = Flask(__name__)

app.register_blueprint(api)

@app.route('/')
def index():
    return "hello world."

# run on port 8000.
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)

