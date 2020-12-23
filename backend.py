from classes import Marketplace, Category, SubCategory


def categories_generate():
    eletronics = Category(1,'Eletronics')
    decoration = Category(2,'Decoration')
    office = Category(3, 'Office')
    categories = [eletronics, decoration, office]

    return categories

def subcategories_generate(categories):
    phone = SubCategory(4, 'Phone', categories[0])
    computer =  SubCategory(5, 'Computer', categories[0])
    art_piece = SubCategory(6, 'Art Piece', categories[1])
    christmas =SubCategory(7, 'Christmas Stuff', categories[1])
    desk = SubCategory(8, 'Desk', categories[2])
    chair = SubCategory(9, 'Chair', categories[2])
    subcategories = [phone,computer,art_piece,christmas,desk,chair]

    return subcategories

def marketplace_generate(categories):
    magalu = Marketplace(1, 'Magalu', categories) 
    b2w = Marketplace(2, 'B2W', categories)
    amazon = Marketplace(3, 'Amazon', categories)
    marketplaces = [magalu,b2w,amazon]
    
    return marketplaces

def list_markeplaces(mktplaces):
    for mktplace in mktplaces:
        print(f'{mktplace.get_id()} - {mktplace.get_name()}')
    
   
def list_categories(mktplace):
    while True:
        try:
            mkt_id = int(input("Id Marketplace: "))
            mkt = search_mkt(mkt_id,mktplace)
            categories = mkt.get_categories()
            for category in categories:
                print(category)
            break
        except ValueError:
            print("Musta be a number")
        except AttributeError:
            print(f'Must be a number between {mktplace[0].get_id()} e {mktplace[-1].get_id()} ')

def list_subcategories(sub):
    while True:
  
        name = input('name of parent category: ')
        category = search_sub(name,sub)
        print(category)
        if category:
            for subcategory in category:
                print(subcategory)
            break
        else:
            print('Category not found!')
        

def search_sub(name,subcategories):
    search_list =[]
    for i in subcategories:
        if i.get_parent_name().lower() == name.lower():
            search_list.append(i)
    return search_list

def web_list_sub(position,category,sub):
    a  = []
    c = category[int(position)]
    name = c.get_name()
    for i in sub:
        if name.lower() == i.get_parent_name().lower():
            a.append(i.get_name())
    return a

def web_list_cat(position,mktplace):
    m = mktplace[int(position)]
    categories = m.get_categories()
    return categories

def search_mkt(id,mktplaces):
    for mktplace in mktplaces:
        if mktplace.get_id() == id:
            return mktplace

def menu():
    options = ['List Marketplaces','List Categories','List SubCategories', 'Sair']
    print('\nMENU: ')

    for i, option in enumerate(options):
        print(f'[{i+1}] - {option}')
    op = int(input('\nSelect an option: '))
    return op

def web_menu():
    marketplaces = {'name': 'Marketplaces', 'route': '/marketplaces'}
    categories = { 'name': 'Categories', 'route': '/categories/99'}
    subcategories = {'name': 'Subcategories', 'route': '/subcategories/99'}
    options = [marketplaces, categories, subcategories]
    return options

