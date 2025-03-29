# Caesar Shift Key Encrytion Algorithm
# To use this code, run it in your terminal as there is no frontend for this program :) 

# Encryption Algorithm
def caesar_cipher_encrypt(user_input):
    # assign alphabet to numbers (a-z,0-25 respectively)
    alphabet_and_numbers = {chr(i + 97): i for i in range(0,26)}
    #get number value of the letter from user_input
    user_input = input('Encrypt text: ').lower().strip()
    result = ''
    for letter in user_input:
            # Check if it's a space 
            if letter == ' ': 
                result += ' ' # keep the space by adding to result variable
            #get number value of the letter
            elif letter in alphabet_and_numbers:
                number_value = alphabet_and_numbers[letter]
        
                #add 3 to the number value(shift)
                shift_3 = add_3(number_value) 
                # Convert back to corresponding letter
                if shift_3 in alphabet_and_numbers.values():
                    key = get_value_from_key(shift_3)
                    result += key
    print(f'Text Encrypted: {result}')
                       
#add 3 to numbers (shift 3)
def add_3(*num):
    for n in num:
        return (n + 3) % 26 # modulo to cover letters beyond 26

# Get key for value 
def get_value_from_key(value):
    alphabet_number = {chr(i + 97) : i for i in range(0,26)}
    for key,value1 in alphabet_number.items():
            if value1 == value :
                return key
        
        
       

# Decryption Algorithm 

def decryption(user_input): 
    dictionary_alphabet = {chr(i + 97): i for i in range(26)}
    user_input = input('Decrypt text: ').lower().strip()
    keep_space = ''
    for letter in user_input: 
        if letter == ' ': 
            keep_space += ' '
        
        elif letter in dictionary_alphabet: 
            letter_number = dictionary_alphabet[letter]
            # subract 3 from letter 
            sub_3 = subract_3(letter_number)
            # get value of the subtraction  
            if sub_3 in dictionary_alphabet.values():
                value_3 = get_value_from_key(sub_3) 
                keep_space += value_3
                
    print(f'Decrypted text: {keep_space}')

# Get key for value 
def get_value_from_key(value):
    alphabet_number = {chr(i + 97) : i for i in range(26)}
    for key,value1 in alphabet_number.items():
            if value1 == value :
                return key

def subract_3(*number):
    for n in number: 
        return (n-3) % 26


# Run the code only when in this file
if __name__ == '__main__':
    user_input1 = input("Choose an option->('E' for Encryption and 'D' for Decryption): ").lower().strip()
    if user_input1.startswith('e'):
        caesar_cipher_encrypt(user_input1)
    elif user_input1.startswith('d'):
        decryption(user_input1)

    else: 
        print(f"Wrong option -> '{user_input1}'")