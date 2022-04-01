from options import *
from registry import available_options


#Get input from user and returns selected
def read_option():
    try:
        option = int(input('Enter your choice: '))
        print()

        return menu_options[option]
    except:
        print('Wrong input. Please enter a number ...')
        return read_option()

menu_options = available_options()

#Prints out menu based on the available_options function
def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key]['name'] )

if __name__=='__main__':
    while(True):
        print_menu()

        option = read_option()
        option['handler'](option) #calls handle_download_url function

        print()
