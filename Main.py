import pwd_encrypt
import getpass
import sys
import os
import keyboard
from colorama import Fore,Back,Style,init
import ui_base as ui
from msvcrt import getch
os.system('mode 800')
ui.CLI()
print("\n\n")
init(convert=True)
cursor=0
choices=["1. Login","2. About"]

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
                os.system('login_module.py')
    elif(cursor==1):
            if key==87 or key==119:
                os.system('CLS')
                cursor=cursor-1
                ui.CLI()
                print("\n\n\n")
                choice()
            elif key==13:
                os.system('aboutDev.py')
             
