#codeing=utf-8
from common import *
app.secret_key = '123456'


queue = Query()
db = queue.conn()
@app.route('/')
def first():
    return app.send_static_file("index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
