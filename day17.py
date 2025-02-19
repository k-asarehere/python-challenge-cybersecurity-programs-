# a simple http request handler in python to 
# fetch and display the content(html) of a webpage 
# no parsing

import requests
def fetch_url(): 
    try: 
        # enter a site name that start with https not http
        enter_site_url = input('Enter the name of the site (for example: khanacademy.org or google.com): ').strip()
        # get khanacademy url 
        site_url = f'https://www.{enter_site_url}'
        get_site_url = requests.get(site_url) 
        # get specific info using BeautifulSoup as a magnifier 
        if get_site_url.status_code == 200:
            print('This is the html content of the url you entered\n') 
            print(get_site_url.content)
        else: 
            print('Server cannot be reached or No internet connection')
    
    except: 
        print('Invalid site name or site protocol must be https not http')

if __name__  == '__main__':
    fetch_url()