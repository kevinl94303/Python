'''
Name: Kevin Li
UNI: krl2134
Date: 4 Nov 2016

encrypt_message takes a string and a key and encrypts the string. 
decrypt_message takes an encrypted string and key and decrypts it. 
search_key returns a list of all possible decryptions of the encrypted
message. encrypt_letter encrypts a text file with a given key. 
decrypt_letter decrypts an encrypted file with the key. 
'''

import string

def encrypt_message(message, key):
    '''takes string message and returns encrypted string with
    each letter shifted by the key'''    
    
    encrypted_message = ""
    
    lower_list = list(string.ascii_lowercase + string.ascii_lowercase)
        #generates list of letters twice (to loop around when encrypting)
    upper_list = list(string.ascii_uppercase + string.ascii_uppercase)
    
    for c in message:
        if c.islower():
            encrypted_message += lower_list[lower_list.index(c) + key]
        elif c.isupper():
            encrypted_message += upper_list[upper_list.index(c) + key]
        else:
            encrypted_message += c #non-letters remain unchanged

    return encrypted_message


def decrypt_message(message, key):
    '''takes encrypted string message and returns decrypted string using
    provided key'''    
    
    decrypted_message = ""
    
    lower_list = list(string.ascii_lowercase)
    upper_list = list(string.ascii_uppercase)
    
    for c in message:
        if c.islower():
            decrypted_message += lower_list[lower_list.index(c) - key]
            #negative indices automatically loop to the end of the list
        elif c.isupper():
            decrypted_message += upper_list[upper_list.index(c) - key]
        else:
            decrypted_message += c #non-letters remain unchanged

    return decrypted_message


def search_key(message):
    '''takes encrypted string message and returns list of every possible
    decryption scheme'''    
    
    possible_results_list = []
    for key in range(1,27):
        possible_results_list.append([key, decrypt_message(message,key)])

    return possible_results_list
    

def encrypt_letter(file_name, key):
    '''procedure which encrypts a text file file_name with a given key in
    a generated file called file_name_encrypted'''
    
    file = open(file_name + ".txt","r")
    encrypted = open(file_name + "_encrypted.txt","w")
    
    file_contents = file.read()
    print(encrypt_message(file_contents,key),file = encrypted)
    
    file.close()
    encrypted.close()

    return None


def decrypt_letter(file_name, key):
    '''procedure which takes an encrypted file called file_name and generates
    a file file_name_decrypted with a given key'''
    
    file = open(file_name + ".txt","r")
    decrypted = open(file_name + "_decrypted.txt","w")
    
    file_contents = file.read()
    print(decrypt_message(file_contents,key),file = decrypted)

    file.close()
    decrypted.close()
    
    return None



if __name__ == '__main__':

    input_s = "Hello Zoe!"
    test_key = 2
    encrypted_s = "Jgnnq Bqg!"
    print("Input:", input_s)
    print("Your encrypted string:", encrypt_message(input_s,test_key))
    print("Expected encrypted string:", encrypted_s)

    print("Input:", encrypted_s)
    print("Your decrypted string:", decrypt_message(encrypted_s,test_key))
    print("Expected decrypted string:", input_s)
    
    encrypt_letter("toEncrypt",2)
    decrypt_letter("toDecrypt",2)
