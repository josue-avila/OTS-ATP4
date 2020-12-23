from flask import Flask, render_template
import backend
from classes import Marketplace, Category, SubCategory

app = Flask(__name__)

app_title = 'Olist List'
category = backend.categories_generate()
subcategory = backend.subcategories_generate(category)
mktplace = backend.marketplace_generate(category)

@app.route('/')
def index():
    marketplaces = {'name': 'Marketplaces', 'route': '/marketplaces'}
    categories = { 'name': 'Categories', 'route': '/categories'}
    subcategories = {'name': 'Subcategories', 'route': '/subcategories'}
    options = [marketplaces, categories, subcategories]
    return render_template('index.html', name = app_title, options = options)

@app.route('/marketplaces')
def mktplaces():
    category = backend.categories_generate()
    #subcategory = backend.subcategories_generate(category)
    mktplace = backend.marketplace_generate(category)

    return render_template('marketplaces.html', mktplace = mktplace, len = len(mktplace), name = app_title )

@app.route('/categories')
def categopries():
    category = backend.categories_generate()
    subcategory = backend.subcategories_generate(category)
    mktplace = backend.marketplace_generate(category)

    return render_template('categories.html', mktplace = mktplace, len = len(mktplace),name = app_title )

@app.route('/categoriesdetail')
def categopriesdetail():
    category = backend.categories_generate()
    subcategory = backend.subcategories_generate(category)
    mktplace = backend.marketplace_generate(category)

    return render_template('categoriesdetail.html', categories = category, len = len(category), name = app_title )


@app.route('/subcategories')
def subategopries():
    category = backend.categories_generate()
    subcategory = backend.subcategories_generate(category)
    mktplace = backend.marketplace_generate(category)

    return render_template('subcategories.html', categories = category, len = len(category),name = app_title )

@app.route('/subcategoriesdetail')
def subategopriesdetail():
    category = backend.categories_generate()
    subcategory = backend.subcategories_generate(category)
    mktplace = backend.marketplace_generate(category)

    return render_template('subcategoriesdetail.html', subcategories = subcategory, len = len(subcategory), name = app_title )


app.run(debug=True)