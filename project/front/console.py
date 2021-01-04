
import sys
sys.path.append('project/')
import back.backend as backend # pylint: disable=import-error

category = backend.categories_gen()
subcategory = backend.subcategories_gen(category)
mktplace = backend.marketplace_gen(category)

while True:
    try:
        option = backend.menu()
        if option == 1:
            backend.save_logs('List marketplaces (console)')
            backend.list_markeplaces(mktplace)
        elif option == 2:
            backend.save_logs('List categories (console)')
            backend.list_categories(mktplace)
        elif option == 3:
            backend.save_logs('List subcategories (console)')
            backend.list_subcategories(subcategory)
        elif option == 4:
            backend.print_logs()
        elif option == 5:
            exit(0)
        else:
            print('Invalid option. Try again')
    except ValueError as err:
        print('Error: ', err)
    except FileNotFoundError as err:
        print('Error: ', err)
