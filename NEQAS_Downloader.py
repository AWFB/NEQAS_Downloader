url_prefix = "https://results.ukneqas.org.uk/output"
url_suffix = '10072/report.pdf'

def handle_download_url(opts):
    dist = input('What distribution do you require? ')
    print()

    url = '/'.join([url_prefix, opts['url_code'], dist, url_suffix])
    print(url)

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
    1: {
        'name': 'Vitamin D',
        'url_code': 'QEHVITD',
        'handler': handle_download_url, # a reference to the function
    },
    2: {
        'name': 'Sweat Tests',
        'url_code': 'QEHSWT',
        'handler': handle_download_url,
    },
    3: {
        'name': 'Exit',
        'url_code': 'QEHVITD/',
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
