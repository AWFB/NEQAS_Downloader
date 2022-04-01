from options import *
from registry import available_options

def read_option():
    try:
        option = int(input('Enter your choice: '))
        print()

        return menu_options[option]
    except:
        print('Wrong input. Please enter a number ...')
        return read_option()

menu_options = available_options()

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key]['name'] )

if __name__=='__main__':
    while(True):
        print_menu()

        option = read_option()
        option['handler'](option)

        print()
