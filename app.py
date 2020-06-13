from flask import *
import mlab

app = Flask(__name__)

mlab.connect()


if __name__ == '__main__':
    app.run(debug=True)
