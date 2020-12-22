from lists import Marketplace

m = ['Magalu','Americanas','Amazon']
categories = ['Eletronics','Decoration','Office']


mktplaces = []


def list_markeplaces():
    for i in m:
        new_id = mktplaces[-1].get_id() + 1 if mktplaces else 1
        mkt = Marketplace(new_id,i,categories)
        mktplaces.append(mkt)
        print(mkt.get_id(), mkt.get_name())
    

def list_categories():
    try:
        mkt_id = int(input("Id Marketplace: "))
        mkt = search_mkt(mkt_id)
        print(mkt.get_categories())
    except ValueError:
        print("Musta be a number")

def search_mkt(id):
    for mkt in mktplaces:
        if mkt.get_id() == id:
            return mkt

def menu():
    options = ['List Marketplaces','List Categories','List SubCategories', 'Sair']
    print('\nMENU: ')

    for i, option in enumerate(options):
        print(f'[{i+1}] - {option}')
    op = int(input('\nSelect an option: '))
    return op

while True:
    try:
        op = menu()
        if op == 1:
            list_markeplaces()
        elif op == 2:
            list_categories()
        elif op == 3:
            print(op)
        elif op == 4:
            exit(0)
        else:
            print('Invalid option. Try again')
    except ValueError as err:
        print('Error: ', err)
    except ZeroDivisionError as ZeroError:
        print('Error: ', ZeroError)