#ADMIN CONSOLE FILE
import os
import ui_base as ui
import extn_encrypt as exencrypt
from colorama import Fore,Back,Style,init
from msvcrt import getch
os.system('CLS')
ui.CLI()
#############################MAIN CODE######################################
session=open("currloginsession.txt","r")
print("Welcome,",session.read(),"\t\t(Admin Console)")
#______________________________MENU____________________________________#

print("\n\n")
init(convert=True)
cursor=0
choices=["1. Billing","2. Close Order(Dine-In Only)","3. Kitchen Mode","4. Make Table Reservation","5. Add to inventory","6. View Inventory","6. Manage Deliveries","7. Manage Reservations","8. Employee Maintanence"]

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
                os.system('bill_module.py')
    elif(cursor==1):
            if key==83 or key==115:
                os.system('CLS')
                cursor=cursor+1
                ui.CLI()
                print("\n\n\n")
                choice()
            if key==87 or key==119:
                os.system('CLS')
                cursor=cursor-1
                ui.CLI()
                print("\n\n\n")
                choice()
            elif key==13:
                os.system('close_orderform.py')
    elif(cursor==2):
            if key==83 or key==115:
                os.system('CLS')
                cursor=cursor+1
                ui.CLI()
                print("\n\n\n")
                choice()
            if key==87 or key==119:
                os.system('CLS')
                cursor=cursor-1
                ui.CLI()
                print("\n\n\n")
                choice()
            elif key==13:
                os.system('kitchen_mode.py')
    elif(cursor==3):
            if key==83 or key==115:
                os.system('CLS')
                cursor=cursor+1
                ui.CLI()
                print("\n\n\n")
                choice()
            if key==87 or key==119:
                os.system('CLS')
                cursor=cursor-1
                ui.CLI()
                print("\n\n\n")
                choice()
            elif key==13:
                os.system('makeResAdm.py')
    elif(cursor==4):
            if key==83 or key==115:
                os.system('CLS')
                cursor=cursor+1
                ui.CLI()
                print("\n\n\n")
                choice()
            if key==87 or key==119:
                os.system('CLS')
                cursor=cursor-1
                ui.CLI()
                print("\n\n\n")
                choice()
            elif key==13:
                os.system('item_add.py')
    elif(cursor==5):
            if key==83 or key==115:
                os.system('CLS')
                cursor=cursor+1
                ui.CLI()
                print("\n\n\n")
                choice()
            if key==87 or key==119:
                os.system('CLS')
                cursor=cursor-1
                ui.CLI()
                print("\n\n\n")
                choice()
            elif key==13:
                os.system('itemModule.py')
    elif(cursor==6):
            if key==83 or key==115:
                os.system('CLS')
                cursor=cursor+1
                ui.CLI()
                print("\n\n\n")
                choice()
            if key==87 or key==119:
                os.system('CLS')
                cursor=cursor-1
                ui.CLI()
                print("\n\n\n")
                choice()
            elif key==13:
                os.system('man_del.py')
    elif(cursor==7):
            if key==83 or key==115:
                os.system('CLS')
                cursor=cursor+1
                ui.CLI()
                print("\n\n\n")
                choice()
            if key==87 or key==119:
                os.system('CLS')
                cursor=cursor-1
                ui.CLI()
                print("\n\n\n")
                choice()
            elif key==13:
                os.system('resMan.py')
    elif(cursor==8):
            if key==87 or key==119:
                os.system('CLS')
                cursor=cursor-1
                ui.CLI()
                print("\n\n\n")
                choice()
            elif key==13:
                os.system('employee_main.py')
