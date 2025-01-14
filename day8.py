# a script that reads a txt file and counts how many lines and words are in the file 

def text_file(file_name):
    try:
        with open(file_name) as file: 
            read_file = file.readlines() 
            number_of_lines = len(read_file)
            number_of_words = sum(len(word.split()) for word in read_file) # convert the file items into a list[..]
            print(f'{file_name} has {number_of_lines} lines and {number_of_words} words!')

    except FileNotFoundError:
        print(f"'{file_name}' is not on your file system or invalid input!")

            
file_name = input('Enter the file name: ').strip()

if __name__ == '__main__':
    text_file(file_name)
          