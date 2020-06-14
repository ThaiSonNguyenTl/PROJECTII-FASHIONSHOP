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

@app.route('/woman')
def woman():
    allproduct = Orderproduct.objects()
    indexnum = 0 
    for product in allproduct:
        indexnum += 1
    # get all document from dabase
    all_clother = Clothers.objects()
    return render_template("woman.html",all_clother= all_clother,indexnum=indexnum)

@app.route('/womandetail/<womanid>', methods = ["GET","POST"])
def womandetail(womanid):
    allproduct = Orderproduct.objects()
    indexnum = 0 
    for product in allproduct:
        indexnum += 1
    woman_id = Clothers.objects.with_id(womanid)
    if request.method == "GET":
        return render_template("womandetail.html",woman_id  = woman_id,indexnum=indexnum )
    else:
        form = request.form
        orderproduct = Orderproduct(
            title = woman_id["title"],
            price = woman_id["price"],
            image = woman_id["image"],
            size = form["size"],
            count = form["count"]
        )
        orderproduct.save() 
        return redirect(url_for('shoppcard'))

if __name__ == '__main__':
    app.run(debug=True)
