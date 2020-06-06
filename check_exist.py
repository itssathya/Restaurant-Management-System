import os
import extn_encrypt as exencrypt
def CheckExist(item,file):
    exencrypt.fileDecrypt(os.getcwd(),'usracc')
    for line in open(file+".txt","r").readlines(): # Read the lines
        info = line.split('|')# Split on the space, and store the results in a list of two strings
        if(item==info[0]):
            exencrypt.fileEncrypt(os.getcwd(),'usracc')
            return False
    exencrypt.fileEncrypt(os.getcwd(),'usracc')
    return True
