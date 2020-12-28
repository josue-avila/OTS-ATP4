from flask import Flask, render_template, redirect
import backend
from classes import Marketplace, Category, SubCategory

app = Flask(__name__)

app_title = 'Olist List'
category = backend.categories_generate()
subcategory = backend.subcategories_generate(category)
mktplace = backend.marketplace_generate(category)

@app.route('/')
def index():
    options = backend.web_menu()
    return render_template('index.html', name = app_title, options = options)

@app.route('/marketplaces')
def mktplaces():
    return render_template('marketplaces.html', mktplace = mktplace, len = len(mktplace), name = app_title )

@app.route('/categories/<mkt>')
def categopries(mkt):
    if int(mkt) < 99:
        cat = backend.web_list_cat(mkt,mktplace)
        return render_template('categories.html', categories = cat, len = len(cat),name = app_title )
    else:
        return redirect('/marketplaces')

@app.route('/subcategories/<cat>')
def subcategories(cat):
    if int(cat) < 99:
        sub = backend.web_list_sub(cat,category, subcategory)
        return render_template('subcategories.html', subcategories= sub, len = len(sub), name = app_title )
    else:
        return redirect('/categories/0')

app.run(debug=True)