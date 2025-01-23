# write a program that interacts with the Github API to fetch user data(like profile information)

# gitub profile info.

# type any github username and you'll get the basic info about that username

import requests  
try:
    user_name = input('Enter your github username: ').strip()
    site_url = requests.get(f'https://api.github.com/users/{user_name}')
    if site_url.status_code == 200: 
        get_user_data = site_url.json()
        print(f'User: {get_user_data['login']}') # github user_name 
        print(f'Name: {get_user_data['name']}') # actual name on github
        print(f'Public Repositories: {get_user_data['public_repos']}')
        print(f'Account creation date: {get_user_data['created_at'][0:10]}') # when the github account was created
        print(f'Followers: {get_user_data['followers']}') # user followers
        print(f'Following: {get_user_data['following']}') # user following
        print(f'Bio: {get_user_data['bio']}') # user bio, 'none' if there isn't any
    else:
        print('Invalid name!') 

except requests.exceptions.ConnectionError:
    print('No internet connection or server not responding')




