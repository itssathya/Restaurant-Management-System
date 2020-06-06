#This module is to encrypt the passwords to Base64 for added security
import base64
def EncryptPass(pwd):
    return base64.b64encode(bytes(pwd, 'utf-8'))
