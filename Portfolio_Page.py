from flask import Flask, render_template, url_for
from flask.ext.bootstrap import Bootstrap

## Resim yollarini saklayan imageDB.py dosyası içe aktarılıyor
from imageDB import imgDB, imageNumber
##

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html', imageNumber=imageNumber)


@app.route('/about')
def about():
    return render_template('about.html', title='About', Aboactive=True)


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact', Conactive=True)


@app.route('/portfolio/<img>')
def single_img(img):
    return render_template('single_img.html', img=img, imgDB=imgDB)


@app.errorhandler(404)
def not_found(a):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)
