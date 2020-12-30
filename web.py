from flask import Flask, render_template, redirect, request
import backend
from classes import Marketplace, Category, SubCategory


app = Flask(__name__)

app_title = 'Olist List'
category = backend.categories_gen()
subcategory = backend.subcategories_gen(category)
mktplace = backend.marketplace_gen(category)

@app.route('/')
def index():
    options = backend.web_menu()
    return render_template('index.html', name = app_title, options = options)

@app.route('/add')
def add():
    return render_template('add.html',categories = category, len = len(category),n = app_title)

@app.route('/add_mkt', methods=['GET','POST'])
def add_mkt():
    name = request.args.get('name')
    categories_names = request.args.keys()
    categories=[]
    for category_name in categories_names:
        cat = backend.search_cat(category_name,category)
        categories.append(cat)
    new_mktplace = backend.new_mktplace(name, categories[1:], mktplace)
    if new_mktplace:
        backend.save_logs('Add new marketplace (web)')
        return f'Succes!'
    else:
        return f'Marketplace already exists!'

@app.route('/marketplaces')
def mktplaces():
    backend.save_logs('List marketplaces (web)')
    return render_template('marketplaces.html', mktplace = mktplace, len = len(mktplace), name = app_title )

@app.route('/categories/<mkt>')
def categopries(mkt):
    cat = backend.web_list_cat(mkt,mktplace)
    return render_template('categories.html', categories = cat, len = len(cat),name = app_title )

@app.route('/allcategories')
def allcategories():
    return render_template('allcategories.html', categories = category, len = len(category),name = app_title)

@app.route('/subcategories/<cat>')
def subcategories(cat):
    sub = backend.web_list_sub(cat,category, subcategory)
    return render_template('subcategories.html', subcategories= sub, len = len(sub), name = app_title )


app.run(debug=True)