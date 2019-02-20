import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC 
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

#message authentication code
def mac(key,source):
    h = hmac.HMAC(key,hashes.SHA256(),default_backend())
    h.update(source)
    return h.finalize()

# Derivar a chave a partir da password usando KDF
def passwd(password,salt):
    backend = default_backend()
    # PBKDF2 derivation function
    kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    # Maximum length for CTR mode 256 bits
    length=32,
    salt=salt,
    iterations=100000,
    backend=backend
    )

    # Encrypt password with PBKDF2
    key = kdf.derive(password)
    # Return key
    return key

# Função de cifrar
def cifrar(mensagem, passphrase):
    salt = os.urandom(16) #salt
    iv = os.urandom(16) #initialization vector
    key= passwd(passphrase,salt)
    #AES in CTR Mode
    cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=default_backend()).encryptor()
    ciphertext = cipher.update(mensagem) + cipher.finalize()
    print(ciphertext)
    #Encrypt-then-MAC
    mc = mac(key,ciphertext)

    #parâmetros da mensagem para envio
    obj = {'ciph' : ciphertext, 'salt' :salt, 'tag' : mc, 'iv' : iv}
    
    return obj

# Função de decifrar
def decifrar(msg, passphrase):
    ciphertext = msg['ciph']
    salt = msg['salt']
    tag = msg['tag']
    iv = msg['iv']
    key = passwd(passphrase,salt)

    #gerar mac utilizando a informação recebida e comparar
    if tag == mac(key,ciphertext):
        #desencriptar
        cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=default_backend()).decryptor()
        plaintext = cipher.update(ciphertext) + cipher.finalize()
        print('Mensagem cifrada:',ciphertext)
        print('Mensagem decifrada:',plaintext)
    else:
        print('Tags diferentes')
        plaintext = b"erro"

    return plaintext