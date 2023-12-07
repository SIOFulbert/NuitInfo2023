#from binascii import hexlify
from hashlib import sha1 as sha1_

def sha1(data):
    h = sha1_()
    h.update(data)
    return h.digest()

def xor(x, y):
    return (int.from_bytes(x, 'little') ^ 
        int.from_bytes(y, 'little')).to_bytes(len(x), 'little')

#Vous aurez besoin de hexlify pour affichier vos octets en hexadécimal.