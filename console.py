import backend

category = backend.categories_generate()
subcategory = backend.subcategories_generate(category)
mktplace = backend.marketplace_generate(category)

while True:
    try:
        op = backend.menu()
        if op == 1:
            backend.list_markeplaces(mktplace)
        elif op == 2:
            backend.list_categories(mktplace)
        elif op == 3:
            backend.list_subcategories(subcategory)
        elif op == 4:
            exit(0)
        else:
            print('Invalid option. Try again')
    except ValueError as err:
        print('Error: ', err)
