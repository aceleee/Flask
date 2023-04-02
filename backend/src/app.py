#codeing=utf-8

import openai
from flask import Flask
from flask import request

app = Flask()

@app.route('/')
def first():
    return app.send_static_file("index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
