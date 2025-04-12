# Symmetric Encryption Program.....same key for encryption and decryption 
# This program encrypt and decrypt messages using one key(for both)

from cryptography.fernet import Fernet 
import ast 


def save_key():
    # store encryption key 
    key = Fernet.generate_key()

    with open('symmetric_key.txt', 'wb') as f: 
        f.write(key)
    return key 





# load symmetric key
def load_symmetric_key(): 
    with open('symmetric_key.txt' , 'rb') as f: 
        read = f.readlines()
        if read: 
            return read[-1]
           
           

# encrypt message
def encrypt_input(message,key):
    fernet_object = Fernet(key)
    encrypt_message = fernet_object.encrypt(message.encode())
    return encrypt_message 

# decrypt message 
def decrypt_input(encrypted_message,key): 
    fernet_object = Fernet(key) 
    decrypt_message = fernet_object.decrypt(encrypted_message).decode()
    return decrypt_message





if __name__ == '__main__':
    save_key()
    key = load_symmetric_key()
    print("\nENTER 'exit' TO EXIT:\n ")

    while True:
        try:
    
            user_input = input("\nDo you want to Encrypt or Decrypt a message?(En for encrypt and De for Decrypt): ").strip().lower()
            if user_input == 'exit':
                break 

            if user_input == 'en': 
                encrypt_message = input('Enter the message you want to encrypt: ').strip()
                encrypt = encrypt_input(encrypt_message,key)
                print('\nEncrypted message: ',encrypt)
                print('Encrypted message key: ',key, '\n')
    

            elif user_input == 'de': 
                decrypt_message = input("Enter the encrypted message you want to decrypt (eg. b'...'):  ").strip()
                encrypted_bytes = ast.literal_eval(decrypt_message)
                decryption_key = input("Enter the encryption key (eg. b'...'): ").strip()
                decryption_bytes = ast.literal_eval(decryption_key)
                decrypt = decrypt_input(encrypted_bytes, decryption_bytes)
                print('Original message: ',decrypt)

            else: 
                print('Invalid input!')
        except: 
            print('Invalid input!')
