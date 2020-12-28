from classes import Marketplace, Category, SubCategory
import datetime

categories_path = 'input/categories.txt'
subcategories_path = 'input/subcategories.txt'
marketplaces_path = 'input/marketplaces.txt'

def dt():
    dt = datetime.datetime.now()
    date = f'Date: {dt.strftime("%d")}/{dt.strftime("%m")}/{dt.strftime("%Y")}'
    time = f'Time: {dt.strftime("%H")}:{dt.strftime("%M")}:{dt.strftime("%S")}'
    date_time = f'{date} - {time}'
    return date_time

def save_logs(operation:str) -> None:
    date_time = dt()
    arquivo = open('logs/logs.txt','a')
    arquivo.write(f'{date_time} - Action: {operation}\n')
    arquivo.close()


def read_categories(path) -> list:
    lista_linhas_arquivo = []
    arquivo = open(path, 'r')
    for linha in arquivo:
        linha_limpa = linha.strip() 
        lista_dados_linha = linha_limpa.split(';') 
        linha_formatada = lista_dados_linha[0]
        lista_linhas_arquivo.append(linha_formatada)
    arquivo.close()
    return lista_linhas_arquivo

def read_mkt_sub(path) -> list:
    lista_linhas_arquivo = []
    arquivo = open(path, 'r')
    for linha in arquivo:
        linha_limpa = linha.strip() 
        lista_dados_linha = linha_limpa.split(';')
        for i in range(len(lista_dados_linha) - 1):
            linha_formatada = [lista_dados_linha[i],lista_dados_linha[i+1]]
            lista_linhas_arquivo.append(linha_formatada)
    arquivo.close()
    return lista_linhas_arquivo

def categories_generate():
    lista = read_categories(categories_path)
    categories =[]
    for i in range(len(lista)):
        categories.append(Category(i+1,lista[i]))

    return categories

def subcategories_generate(categories):
    subcategories = []
    lista = read_mkt_sub(subcategories_path)
    for i in range(len(lista)):
        subcategories.append(SubCategory(i+4,lista[i][0],eval(lista[i][1])))

    return subcategories

def marketplace_generate(categories):
    marketplaces = []
    lista = read_mkt_sub(marketplaces_path)
    for i in range(len(lista)):
        marketplaces.append(Marketplace(i+1,lista[i][0],eval(lista[i][1])))
    return marketplaces

def list_markeplaces(mktplaces):
    save_logs('List marketplaces (console)')
    for mktplace in mktplaces:
        print(f'{mktplace.get_id()} - {mktplace.get_name()}')
    
   
def list_categories(mktplace):
    save_logs('List categories (console)')
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
    save_logs('List subcategories (console)')
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
    save_logs('List subcategories (web)')
    a  = []
    c = category[int(position)]
    name = c.get_name()
    for i in sub:
        if name.lower() == i.get_parent_name().lower():
            a.append(i.get_name())
    return a

def web_list_cat(position,mktplace):
    save_logs('List categories (web)')
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

