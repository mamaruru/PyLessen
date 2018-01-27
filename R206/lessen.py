'''
Created on 2018/01/26

@author: 0ashi
'''
import string
import random

from Crypto.Cipher import AES

def main():
    print(AES.block_size)
    print(string.ascii_letters)
    
    key = ''.join(
        random.choice(string.ascii_letters) for _ in  range(AES.block_size)) 
    
    iv = ''.join(
        random.choice(string.ascii_letters) for _ in  range(AES.block_size))
    
    plaintext = 'fgfdfhsgfshdfjhsdfkjjh'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padding_length = AES.block_size - len(plaintext) % AES.block_size
    plaintext += chr(padding_length) * padding_length
    cipher_text = cipher.encrypt(plaintext)
    print(cipher_text)
    print(plaintext)
    print('ABC')

    
    
    
if __name__ == '__main__':
    main()
    