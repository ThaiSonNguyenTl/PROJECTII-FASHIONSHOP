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
    return render_template("index.html", indexnum=indexnum)


@app.route('/woman')
def woman():
    # get all document from dabase
    all_clother = Clothers.objects()
    return render_template("woman.html", all_clother=all_clother)


@app.route('/womandetail/<womanid>', methods=["GET", "POST"])
def womandetail(womanid):

    woman_id = Clothers.objects.with_id(womanid)
    if request.method == "GET":
        return render_template("womandetail.html", woman_id=woman_id)
    else:
        form = request.form
        orderproduct = Orderproduct(
            title=woman_id["title"],
            price=woman_id["price"],
            image=woman_id["image"],
            size=form["size"],
            count=form["count"]
        )
        orderproduct.save()
        return redirect(url_for('shoppcard'))


@app.route('/man')
def man():
    allproduct = Orderproduct.objects()
    indexnum = 0
    for product in allproduct:
        indexnum += 1
    all_clothman = Mancloth.objects()
    return render_template("man.html", all_clothman=all_clothman, indexnum=indexnum)


@app.route('/detail/<imgid>', methods=["GET", "POST"])
def detail(imgid):
    allproduct = Orderproduct.objects()
    indexnum = 0
    for product in allproduct:
        indexnum += 1
    img_id = Mancloth.objects.with_id(imgid)
    if request.method == "GET":
        return render_template("detail.html", img_id=img_id, indexnum=indexnum)
    else:
        form = request.form
        orderproduct = Orderproduct(
            title=img_id["title"],
            price=img_id["price"],
            image=img_id["image"],
            size=form["size"],
            count=form["count"]
        )
        orderproduct.save()
        return redirect(url_for('shoppcard'))


if __name__ == '__main__':
    app.run(debug=True)
