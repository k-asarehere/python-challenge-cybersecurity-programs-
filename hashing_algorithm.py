"""a py script that hashes a user file document.
Use Case: When you have a document file and you want to know whether it has been modified or not,
you first have to hash the document(using this program) and after that keep the hash values(64 fixed-size string characters) somewhere. Then, as time goes on or 
when you get suspicion that the document file has lost it's integrity, you again run it through this program. When the hash values are different(with the previous hash values you kept somewhere) it means the document file has indeed 
been modified and has lost it's integrity.....,"""


from pathlib import Path
import hashlib
import base64
def encode_doc(document): 
    # Check doc on os
    file_path = f'C:/Users/YANKEY123/Documents/{document}' # insert your document path here as it is here --> (C:/insert yours/insert yours/Documents/)
    doc_on_os = Path(file_path)
    # Open document
    if doc_on_os.exists():
        with open(doc_on_os, 'rb') as f:
            # Encode document
            encode_document = base64.b64encode(f.read())
        return encode_document
    else:
        return f"'{document}' not found on your device."
    


# Hashing the document using encode_doc function 
def hash_document(doc): 
    try:
        hash_doc = hashlib.sha256(doc).hexdigest()
        return hash_doc
    except:
        return 'Invalid input'



  
user_input = input('Upload the document file to hash: ').strip()
encoded_data = encode_doc(user_input) 
hash_data = hash_document(encoded_data)
print(hash_data)
