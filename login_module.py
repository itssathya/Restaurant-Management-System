#Login Module for both ADMIN and USER
import pwd_encrypt
import extn_encrypt as exencrypt
import getpass
import sys
import os
import keyboard
from colorama import Fore,Back,Style,init
import ui_base as ui
from msvcrt import getch
import auth_module as oauth
os.system('CLS')
ui.CLI()
print("\n\n")
###############################__MAIN PROGRAM__###########################
def login():
    uname=input("Username: ")
    pwd=getpass.getpass("Password: ")
    print(Fore.GREEN+Style.BRIGHT+"Authenticating Credentials..."+Style.RESET_ALL+Fore.WHITE)
    exencrypt.fileDecrypt(os.getcwd(),'usracc')
    exencrypt.fileDecrypt(os.getcwd(),'adminacc')
    checksum=oauth.auth(uname,pwd)
    exencrypt.fileEncrypt(os.getcwd(),'usracc')
    exencrypt.fileEncrypt(os.getcwd(),'adminacc')
    if(checksum=='TrueAdmin'):
        with open("currloginsession.txt","w") as writesession:
            writesession.write(uname)
        os.system("admin_console.py")
    elif(checksum=='TrueUser'):
        os.system('makeRes.py')
        input()
    elif(checksum==False):
        print(Fore.RED+Style.BRIGHT+"Username/Password does not match. Both username and password are case-sensitive.")
        input(Style.BRIGHT+"Press any key to retry..."+Style.RESET_ALL+Fore.WHITE)
        os.system("login_module.py")
#######################################PRE INTERFACE#######################
print("\n\n")
init(convert=True)
cursor=0
choices=["1. Login","2. Register"]

def choice():
    curform= Back.WHITE + Fore.BLACK + choices[cursor]+ Style.RESET_ALL
    for i in range (len(choices)):
        if (i==cursor):
            print(curform)
            continue
        print(choices[i])
choice()
while(True):
    key = ord(getch())
    if(cursor==0):
            if key==83 or key==115:
                os.system('CLS')
                cursor=cursor+1
                ui.CLI()
                print("\n\n\n")
                choice()
            elif key==13:
                login()
    elif(cursor==1):
            if key==87 or key==119:
                os.system('CLS')
                cursor=cursor-1
                ui.CLI()
                print("\n\n\n")
                choice()
            elif key==13:
                os.system('user_regmodule.py')
             


    
