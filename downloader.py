import requests
import LoginDetails

url_prefix = "https://results.ukneqas.org.uk/output"
url_suffix = '10072/report.pdf'

user = LoginDetails.username
password = LoginDetails.password

def handle_download_url(opts):
    dist = input('What distribution do you require? ')
    print()

    url = '/'.join([url_prefix, opts['url_code'], dist, url_suffix])
    print(url)

    r = requests.get(url, auth=(user, password), allow_redirects=True)
    
    filename = ' '.join([opts['name'], dist, '.pdf'])
 
    with open(filename,'wb') as output_file:
        output_file.write(r.content)
    

