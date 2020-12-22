from lists import Marketplace, Category, SubCategory


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
        try:
            id = int(input('Id of parent category: '))
            category = search_sub(id,sub)
            for subcategory in category:
                print(subcategory)
            break
        except ValueError:
            print("Musta be a number")
        except AttributeError:
            print(f'Must be a number between {sub[0].get_parent_id()} e {sub[-1].get_parent_id()} ')

def search_sub(id,subcategories):
    search_list =[]
    for i in subcategories:
        if i.get_parent_id() == id:
            search_list.append(i)
    return search_list

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

category = categories_generate()
subcategory = subcategories_generate(category)
mktplace = marketplace_generate(category)

while True:
    try:
        op = menu()
        if op == 1:
            list_markeplaces(mktplace)
        elif op == 2:
            list_categories(mktplace)
        elif op == 3:
            list_subcategories(subcategory)
        elif op == 4:
            exit(0)
        else:
            print('Invalid option. Try again')
    except ValueError as err:
        print('Error: ', err)
