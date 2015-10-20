### Python
import sys
from datetime import datetime
### Flask
from flask import Flask, \
    render_template, \
    url_for, \
    session, \
    g
### Flask.ext
from flask.ext.bootstrap import Bootstrap

### My
from content_DB import Content

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top secret!'
bootstrap = Bootstrap(app)

Content_DB = Content()

@app.before_request
def before_request():
    if not 'count' in session:
        session['count'] = 1

    else:
        session['count'] += 1

    g.when = datetime.now().strftime('%H:%M:%S')


@app.route('/')
def index():

    ##
    # contend_DB.py ID sort
    con_id_list = []
    for e_id in Content_DB:
        con_id_list.append(Content_DB[e_id]['ID'])

    srt_con_id_list = sorted(con_id_list, reverse=True)
    #print(type(srt_con_id_list[0]))

    # contend_DB.py ID Convert int() | str()
    srt_str_con_id_list = []
    for e_id_cnvrt in srt_con_id_list:
        e_id_str = str(e_id_cnvrt)
        srt_str_con_id_list.append(e_id_str)
    #print(type(srt_str_con_id_list[0]))
    ##

    ##
    # Python Version
    ##
    pyVer = sys.version

    return render_template('index.html',
                           Content_DB=Content_DB,
                           con_id_list=con_id_list,
                           srt_str_con_id_list=srt_str_con_id_list,
                           count=session['count'],
                           when=g.when,
                           pyVer=pyVer)


@app.route('/about')
def about():
    return render_template('about.html',
                           title='About',
                           Aboactive=True)


@app.route('/contact')
def contact():
    return render_template('contact.html',
                           title='Contact',
                           Conactive=True)


@app.route('/<page>')
def single_img(page):

    if page == Content_DB['cont_01']['link']:
        return render_template('single_img.html',
                               con_id=Content_DB['cont_01']['ID'],
                               con_thumb=Content_DB['cont_01']['thumb'],
                               con_bigPic=Content_DB['cont_01']['bigPic'],
                               con_title=Content_DB['cont_01']['title'],
                               con_text=Content_DB['cont_01']['text'])

    if page == Content_DB['cont_02']['link']:
        return render_template('single_img.html',
                               con_id=Content_DB['cont_02']['ID'],
                               con_thumb=Content_DB['cont_02']['thumb'],
                               con_bigPic=Content_DB['cont_02']['bigPic'],
                               con_title=Content_DB['cont_02']['title'],
                               con_text=Content_DB['cont_02']['text'])

    if page == Content_DB['cont_03']['link']:
        return render_template('single_img.html',
                               con_id=Content_DB['cont_03']['ID'],
                               con_thumb=Content_DB['cont_03']['thumb'],
                               con_bigPic=Content_DB['cont_03']['bigPic'],
                               con_title=Content_DB['cont_03']['title'],
                               con_text=Content_DB['cont_03']['text'])

    if page == Content_DB['cont_04']['link']:
        return render_template('single_img.html',
                               con_id=Content_DB['cont_04']['ID'],
                               con_thumb=Content_DB['cont_04']['thumb'],
                               con_bigPic=Content_DB['cont_04']['bigPic'],
                               con_title=Content_DB['cont_04']['title'],
                               con_text=Content_DB['cont_04']['text'])

    if page == Content_DB['cont_05']['link']:
        return render_template('single_img.html',
                               con_id=Content_DB['cont_05']['ID'],
                               con_thumb=Content_DB['cont_05']['thumb'],
                               con_bigPic=Content_DB['cont_05']['bigPic'],
                               con_title=Content_DB['cont_05']['title'],
                               con_text=Content_DB['cont_05']['text'])

    if page == Content_DB['cont_06']['link']:
        return render_template('single_img.html',
                               con_id=Content_DB['cont_06']['ID'],
                               con_thumb=Content_DB['cont_06']['thumb'],
                               con_bigPic=Content_DB['cont_06']['bigPic'],
                               con_title=Content_DB['cont_06']['title'],
                               con_text=Content_DB['cont_06']['text'])

    if page == Content_DB['cont_07']['link']:
        return render_template('single_img.html',
                               con_id=Content_DB['cont_07']['ID'],
                               con_thumb=Content_DB['cont_07']['thumb'],
                               con_bigPic=Content_DB['cont_07']['bigPic'],
                               con_title=Content_DB['cont_07']['title'],
                               con_text=Content_DB['cont_07']['text'])

    if page == Content_DB['cont_08']['link']:
        return render_template('single_img.html',
                               con_id=Content_DB['cont_08']['ID'],
                               con_thumb=Content_DB['cont_08']['thumb'],
                               con_bigPic=Content_DB['cont_08']['bigPic'],
                               con_title=Content_DB['cont_08']['title'],
                               con_text=Content_DB['cont_08']['text'])

    if page == Content_DB['cont_09']['link']:
        return render_template('single_img.html',
                               con_id=Content_DB['cont_09']['ID'],
                               con_thumb=Content_DB['cont_09']['thumb'],
                               con_bigPic=Content_DB['cont_09']['bigPic'],
                               con_title=Content_DB['cont_09']['title'],
                               con_text=Content_DB['cont_09']['text'])

    if page == Content_DB['cont_010']['link']:
        return render_template('single_img.html',
                               con_id=Content_DB['cont_010']['ID'],
                               con_thumb=Content_DB['cont_010']['thumb'],
                               con_bigPic=Content_DB['cont_010']['bigPic'],
                               con_title=Content_DB['cont_010']['title'],
                               con_text=Content_DB['cont_010']['text'])


    if page == Content_DB['cont_011']['link']:
        return render_template('single_img.html',
                               con_id=Content_DB['cont_011']['ID'],
                               con_thumb=Content_DB['cont_011']['thumb'],
                               con_bigPic=Content_DB['cont_011']['bigPic'],
                               con_title=Content_DB['cont_011']['title'],
                               con_text=Content_DB['cont_011']['text'])


@app.errorhandler(404)
def not_found(a):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
