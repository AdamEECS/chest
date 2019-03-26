from flask import Flask
from flask import jsonify
import random

app = Flask(__name__)


@app.route('/api')
def hello_world():
    l = [1, 2, 3]
    r = random.choice(l)
    return jsonify(r)


if __name__ == '__main__':
    app.debug = True
    app.run()
