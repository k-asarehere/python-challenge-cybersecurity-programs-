# a python script that fetches data from a public API(e.g.,OpenWeatherMap) and displays the weather

# degrees in celcius

import requests

# catch any input error
try: 
    place_name = input('Enter a city name: ').title().strip()
    api_key = 'b10ff11e4e44c72dfdb65f0f35b2c0e0' # get the api key so the request library can get the weather data
    site_url = 'https://api.openweathermap.org/data/2.5/weather' # base url for api in openweathermap
    # specifying the weather data query
    specific_query = {
        "q" : f"{place_name}",
        "appid" : "b10ff11e4e44c72dfdb65f0f35b2c0e0",
        "units" : "metric"

    }
    get_api = requests.get(site_url,params=specific_query)
    get_api_data = get_api.json() # convert the weather data into json
    get_weather_info = get_api_data
    # retrieve weather specific info
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
