from classes import Marketplace, Category, SubCategory
import datetime

categories_path = 'input/categories.txt'
subcategories_path = 'input/subcategories.txt'
marketplaces_path = 'input/marketplaces.txt'

# console + web
def marketplace_gen(categories: list) -> list:
    marketplaces = []
    input_mkt = read_input(marketplaces_path)
    for i in range(len(input_mkt)):
        mkt = Marketplace(i +1,input_mkt[i][0],eval(input_mkt[i][1]))
        marketplaces.append(mkt)
    return marketplaces

def categories_gen() -> list:
    input_cat = read_input(categories_path)
    categories = []
    for i in range(len(input_cat)):
        categories.append(Category(i + 7,input_cat[i][0]))
    return categories

def subcategories_gen(categories) -> list:
    subcategories = []
    input_sub = read_input(subcategories_path)
    for i in range(len(input_sub)):
        sub = SubCategory(i + 7,input_sub[i][0],eval(input_sub[i][1]))
        subcategories.append(sub)
    return subcategories

def instant_datetime() -> str:
    dt = datetime.datetime.now()
    date = f'{dt.strftime("%d")}/{dt.strftime("%m")}/{dt.strftime("%Y")}'
    time = f'{dt.strftime("%H")}:{dt.strftime("%M")}:{dt.strftime("%S")}'
    date_time = f'{date};{time}'
    return date_time

def save_logs(operation:str) -> None:
    date_time = instant_datetime()
    arquivo = open('logs/logs.txt','a')
    arquivo.write(f'{date_time};{operation}\n')
    arquivo.close()

def read_input(path:str) -> list:
    lista_linhas_arquivo = []
    arquivo = open(path, 'r')
    for linha in arquivo:
        linha_limpa = linha.strip() 
        lista_dados_linha = linha_limpa.split(';')
        lista_linhas_arquivo.append(lista_dados_linha)
    arquivo.close()
    return lista_linhas_arquivo

def read_logs():
    try:
        log_list =[]
        file = open('logs/logs.txt','r')
        for line in file:
            clean_line = line.strip(';')
            list_data_line = clean_line.split(';')
            formataded = f'Date: {list_data_line[0]} Time: {list_data_line[1]} Action: {list_data_line[2]}'
            log_list.append(formataded)
        return log_list
    except:
        raise FileNotFoundError('There is no logs yet!')

def print_logs():
    logs = read_logs()
    while True:
        try:
            tail = int(input('Number of elements u want to see (Zero to view all of them): '))
            if tail > 0:
                for log in logs[-tail:]:
                    print(log)
                break
            elif tail == 0:
                for log in logs:
                    print(log)
                break   
            else:
                print('Needs to be a valid number (greater then zero)')
        except:
            raise ValueError('Needs to be a valid number (greater then zero)')

# console 
def log_menu():
    options = ['Filter by Date','Filter by Action','Sair']
    print('\nMENU: ')
    for i, option in enumerate(options):
        print(f'[{i+1}] - {option}')
    option = int(input('\nSelect an option: '))
    return option

def menu() -> int:
    options = ['List Marketplaces','List Categories','List SubCategories', 'Logs','Sair']
    print('\nMENU: ')
    for i, option in enumerate(options):
        print(f'[{i+1}] - {option}')
    option = int(input('\nSelect an option: '))
    return option

def list_markeplaces(mktplaces: Marketplace) -> None:
    for mktplace in mktplaces:
        print(f'{mktplace.get_id()} - {mktplace.get_name()}')
    
def list_categories(mktplace:list) -> None:
    while True:
        name = input("Name of marketplace: ")
        mkt = search_mkt(name,mktplace)
        if mkt:   
            categories = mkt.get_categories()
            for category in categories:
                print(category)
            break
        else:
            print('Marketplace not found!')
            
def list_subcategories(sub:list) -> None:
    while True:
        name = input('Name of parent category: ')
        category = search_sub(name,sub)
        if category:
            for subcategory in category:
                print(subcategory)
            break
        else:
            print('Category not found!')

def search_sub(name:str,subcategories:list) -> list:
    search_list =[]
    for i in subcategories:
        if i.get_parent_name().lower() == name.lower():
            search_list.append(i)
    return search_list

def search_mkt(name:str,mktplaces:list) -> Marketplace:
    for mktplace in mktplaces:
        if mktplace.get_name().lower() == name.lower():
            return mktplace

# web
def web_menu() -> list:
    marketplaces = {'name': 'Marketplaces', 'route': '/marketplaces'}
    categories = { 'name': 'Categories', 'route': '/marketplaces'}
    subcategories = {'name': 'Subcategories', 'route': '/allcategories'}
    options = [marketplaces, categories, subcategories]
    return options

def web_list_cat(name:str,mktplace:list) -> list:
    save_logs('List categories (web)')
    for i in mktplace:
        if i.get_name().lower() == name.lower():
            categories = i.get_categories()
    return categories  

def web_list_sub(name:str,categories:list,sub:list) -> list:
    save_logs('List subcategories (web)')
    subcategories = []
    for i in sub:
        if i.get_parent_name().lower() == name.lower():
            subcategories.append(i)
    return subcategories
   