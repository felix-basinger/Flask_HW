from flask import Flask
from flask import render_template

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
