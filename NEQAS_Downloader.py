from numpy import full
import dictionary as dic

url = "https://results.ukneqas.org.uk/output/"
end_of_url = '/10072/report.pdf'

menu_options = {
    1: 'Vitamin D',
    2: 'Sweat Tests',
    3: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

# Fetch url code from dictionary 
def vitamin_D ():
    dist = input('What distribution do you require? ')
    print(url + dic.VITD['url_code'] + dist + end_of_url)
    exit()

def sweat_test():
    dist = input('What distribution do you require? ')
    print(url + dic.SWEAT['url_code'] + dist + end_of_url)

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        
        #Check what choice was entered and act accordingly
        if option == 1:
            vitamin_D()
        elif option == 2:
            sweat_test()
            break
        elif option == 3:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option')
