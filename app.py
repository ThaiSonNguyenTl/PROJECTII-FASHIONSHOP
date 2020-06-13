from flask import *
import mlab

app = Flask(__name__)

mlab.connect()

@app.route('/')
def index():
    allproduct = Orderproduct.objects()
    indexnum = 0 
    for product in allproduct:
        indexnum += 1
    return render_template("index.html",indexnum=indexnum)


if __name__ == '__main__':
    app.run(debug=True)
