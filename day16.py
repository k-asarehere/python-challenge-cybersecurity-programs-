# a program that scrapes a website(eg. news healines from a news site) and displays the results
# this program gets the first news headline from the BBC website 
import requests 
from bs4 import BeautifulSoup as bs # bs for simplicity so i won't be writing BeautifulSoup in full 

try:
    url = 'https://www.bbc.co.uk'
    response = requests.get(url) 
    # analyze/parse the html content for specific info 
    analyze = bs(response.text, 'html.parser')
    retrieve_info = analyze.find('h3') # gets the first headline found on the BBC homepage
    print(retrieve_info.get_text())
    
    

except requests.exceptions.ConnectionError:
    print('No internet connection or server can not be reached')

except: 
    print('Server can not be reached')
