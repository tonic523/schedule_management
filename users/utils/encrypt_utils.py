import base64

import my_settings

from Cryptodome.Cipher import AES
from Crypto.Util.Padding import pad
from Cryptodome import Random
from Cryptodome.Protocol.KDF import PBKDF2

BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) %  BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

def encrypt(information, key):
    key = key.encode('utf-8')
    information = pad(information).encode('utf-8')
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    result = base64.b64encode(iv + cipher.encrypt(information))
    print(result)
    return result

def decrypt(information, key):
    key = key.encode('utf-8')
    information = base64.b64decode(information)
    iv = information[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.decrypt(information[16:]).decode('utf-8')

def encryption(user_input):
    return encrypt(user_input, my_settings.KEY)

def decryption(information):
    return decrypt(information, my_settings.KEY)