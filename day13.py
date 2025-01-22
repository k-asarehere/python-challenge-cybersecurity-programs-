# a python script that fetches data from a public API(e.g.,OpenWeatherMap) and displays the weather

# degrees in celcius

import requests


try: 
    place_name = input('Enter a city name: ').title().strip()
    api_key = 'b10ff11e4e44c72dfdb65f0f35b2c0e0'
    site_url = 'https://api.openweathermap.org/data/2.5/weather'
    specific_query = {
        "q" : f"{place_name}",
        "appid" : "b10ff11e4e44c72dfdb65f0f35b2c0e0",
        "units" : "metric"

    }
    get_api = requests.get(site_url,params=specific_query)
    get_api_data = get_api.json()
    get_weather_info = get_api_data
    temperature = get_weather_info['main']
    temperature_of_place = temperature['temp']
    country_or_city_name_info = get_weather_info['sys']
    get_country_or_city_name = country_or_city_name_info['country']
    print(f'Place: {place_name}')
    print(f'Country: {get_country_or_city_name}')
    print(f'Temperature/Weather: {temperature_of_place}')
    
    
    


except requests.exceptions.ConnectionError:
    print('No internet connection or server is not running')
except KeyError:
    print('Invalid input! Try again')
