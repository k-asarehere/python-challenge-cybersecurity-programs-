# a script that reads a txt file and counts how many lines and words are in the file 
# names.txt is already on my local pc 
#from collections import Counter
'''text.txt file:
script for writing into text.txt file
with open('text.txt', 'a') as f:
    name = input('Enter your name: ').title()
    f.write(f'{name}\n')

# was entered manually from the prompt 
1     2
John Doe
3
Kwasi
4
Kwadwo
5
Ken
6
Evelyn
7        8
Kennedy Asare
9       10
Frank Asare
11     12
Afia Asare
13
Lordina 
14       15
Amankwa Asare
16          17
Perpertual Asare
== 11 lines
'''
file_name = 'text.txt'
with open(file_name) as f: # default is read('r')
    read_file = f.readlines() 
    number_of_lines = len(read_file)
    number_of_words = sum(len(word.split()) for word in read_file) # convert the file items into a list[..]
    print(f'{file_name} file has {number_of_lines} lines and {number_of_words} words')
   
    
    
        