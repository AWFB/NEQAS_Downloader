import vitamin_d
import sweat_test

def handle_exit(opts):
    # this one doesn't need the opts at all, but we have a unified way of calling an option function, so it needs be the same
    print('Thanks message before exiting')
    exit()

def read_option():
    try:
        option = int(input('Enter your choice: '))
        print()

        return menu_options[option]
    except:
        print('Wrong input. Please enter a number ...')
        return read_option()

menu_options = {
    1: vitamin_d.option,
    2: sweat_test.option,
    3: {
        'name': 'Exit',
        'handler': handle_exit,
    }
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key]['name'] )

if __name__=='__main__':
    while(True):
        print_menu()

        option = read_option()
        # call the function in the option, passing in the option, so you can get the 'url_code' or other options inside it
        option['handler'](option)

        print()
