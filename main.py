from flask import Flask, url_for
from flask import render_template, request, make_response, redirect

app = Flask(__name__)

PRODUCTS = [{'category': 'Куртка',
             'model': 'Осенняя',
             'ID': '1233214567',
             },

            {'category': 'Куртка',
             'model': 'Зимняя',
             'ID': '1233224543',
             },

            {'category': 'Куртка',
             'model': 'Весенняя',
             'ID': '1233228539',
             },

            {'category': 'Обувь',
             'model': 'Беговая',
             'ID': '1233238039',
             },

            {'category': 'Обувь',
             'model': 'Походная',
             'ID': '1233246523',
             },

            {'category': 'Обувь',
             'model': 'Туфли',
             'ID': '1233028012',
             }, ]


@app.route('/')
def products():
    context = {'products': PRODUCTS}
    return render_template('products.html', **context)


@app.route('/jackets/')
def jackets():
    context = {'jackets': PRODUCTS}
    return render_template('jackets.html', **context)


@app.route('/shoes/')
def shoes():
    context = {'shoes': PRODUCTS}
    return render_template('shoes.html', **context)


@app.route('/submit/', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        mail = request.form.get('email')
        response = make_response(render_template('answer.html', name=name, mail=mail))
        response.set_cookie('username', name)
        response.set_cookie('mail', mail)
        return response
    return render_template('form.html')


@app.route('/cookie_del', methods=['GET', 'POST'])
def cookie_del():
    name = request.form.get('username')
    mail = request.form.get('mail')
    response = make_response(redirect(url_for('submit')))
    response.delete_cookie('username', name)
    response.delete_cookie('mail', mail)
    return response

