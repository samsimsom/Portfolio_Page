from flask import Flask, \
    render_template, \
    url_for, \
    request, \
    redirect

from flask.ext.bootstrap import Bootstrap

##
from content_DB import Content
##

# from page_creator import page_ID_list

app = Flask(__name__)
bootstrap = Bootstrap(app)

Content_DB = Content()

@app.route('/')
def index():
    params = request.args.items()
    return render_template('index.html', Content_DB=Content_DB, params=params)


@app.route('/about')
def about():
    return render_template('about.html', title='About', Aboactive=True)


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact', Conactive=True)


@app.route('/portfolio/<page>')
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


@app.errorhandler(404)
def not_found(a):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)
