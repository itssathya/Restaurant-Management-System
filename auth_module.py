#Authentication Platform
import pwd_encrypt as pe
def auth(uname,pwd):
   
    for line in open("usracc.txt","r").readlines(): # Read the lines
        login_info = line.split('|')# Split on the space, and store the results in a list of two strings
        if(uname==login_info[0] and login_info[1]==str(pe.EncryptPass(pwd))):
            return 'TrueUser'
    
    for line in open("adminacc.txt","r").readlines(): # Read the lines
        login_info = line.split('|') # Split on the space, and store the results in a list of two strings
        if(uname==login_info[0] and login_info[1]== str(pe.EncryptPass(pwd))):
            return 'TrueAdmin'
    return False
