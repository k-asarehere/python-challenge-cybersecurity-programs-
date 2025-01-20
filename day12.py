# a script that reads a JSON file and prints out specific values based on user input
# json file # retrieve specific info based on input 

import json # json library to work with json
def json_file(file_name, user_input):
    # catch any invalid input by user
    try: 
        with open(file_name) as json_file:
            info = json.load(json_file)
            value = info[f'{user_input}']
            print(value)

    except FileNotFoundError:
       print(f"'{file_name}' file not found on your device")
            
    except KeyError:
        print(f"'{user_input}' not in json file")
    
    except:
       print('Invalid Input')

# values from user
if __name__ == '__main__':
    file_name = input('Enter the name of your json file: ').strip()
    user_input = input('Enter the value you want from your json file: ').strip()
    json_file(file_name,user_input)