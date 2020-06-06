#Extension Encryption for User Data Files
import pyAesCrypt
import os
def fileEncrypt(dir,file):
    orig=dir+"\\"+file+".txt"
    fin=dir+"\\"+file+".txt.aes"
    bufferSize = 64 * 1024
    password="cmVzdG1hbnBhc3N3b3Jk"
    pyAesCrypt.encryptFile(orig, fin, password, bufferSize)
    os.remove(orig)
def fileDecrypt(dir,file):
    orig=dir+"\\"+file+".txt.aes"
    fin=dir+"\\"+file+".txt"
    bufferSize = 64 * 1024
    password="cmVzdG1hbnBhc3N3b3Jk"
    pyAesCrypt.decryptFile(orig, fin, password, bufferSize)
    os.remove(orig)

