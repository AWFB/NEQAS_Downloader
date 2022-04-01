import requests 

url_prefix = "https://results.ukneqas.org.uk/output"
url_suffix = '10072/report.pdf'

def handle_download_url(opts):
    dist = input('What distribution do you require? ')
    print()

    url = '/'.join([url_prefix, opts['url_code'], dist, url_suffix])
    print(url)

    r = requests.get(url)
    filename = url.split('/')[-1] # this will take only -1 splitted part of the url
 
    with open(filename,'wb') as output_file:
        output_file.write(r.content)