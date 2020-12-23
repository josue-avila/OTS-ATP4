from flask import Flask, render_template
import backend
from classes import Marketplace, Category, SubCategory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/marketplaces')
def mktplaces():
    category = backend.categories_generate()
    subcategory = backend.subcategories_generate(category)
    mktplace = backend.marketplace_generate(category)

    return render_template('marketplaces.html', mktplace = mktplace, len = len(mktplace) )

@app.route('/categories')
def categopries():
    category = backend.categories_generate()
    subcategory = backend.subcategories_generate(category)
    mktplace = backend.marketplace_generate(category)

    return render_template('categories.html', mktplace = mktplace, len = len(mktplace))

@app.route('/categoriesdetail')
def categopriesdetail():
    category = backend.categories_generate()
    subcategory = backend.subcategories_generate(category)
    mktplace = backend.marketplace_generate(category)

    return render_template('categoriesdetail.html', categories = category, len = len(category))


@app.route('/subcategories')
def subategopries():
    category = backend.categories_generate()
    subcategory = backend.subcategories_generate(category)
    mktplace = backend.marketplace_generate(category)

    return render_template('subcategories.html', categories = category, len = len(category))

@app.route('/subcategoriesdetail')
def subategopriesdetail():
    category = backend.categories_generate()
    subcategory = backend.subcategories_generate(category)
    mktplace = backend.marketplace_generate(category)

    return render_template('subcategoriesdetail.html', subcategories = subcategory, len = len(subcategory) )


app.run(debug=True)