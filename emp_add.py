import os
import keyboard
from colorama import Fore,Back,Style,init
import ui_base as ui
from msvcrt import getch
os.system('CLS')
ui.CLI()
init(convert=True)
cursor=0
choices=["1.Cashier","2.Chef","3.Server","4.Online"]
curform= Back.WHITE + Fore.BLACK + choices[cursor]+ Style.RESET_ALL
def Empdetails(empname,DOB,phno,email,empno):
    file=open("employee_record.txt","a")
    file.write(empname)
    file.write("|")
    file.write(DOB)
    file.write("|")
    file.write(str(phno))
    file.write("|")
    file.write(email)
    file.write("|")
    file.write(empno)
    file.write("\n")
    file.close()
    os.system('admin_console.py')

def choice():
    for i in range (len(choices)):
        if (i==cursor):
            print(curform)
            continue
        print(choices[i])
    
def genEMPNO(value):
        add=open("enoadd.txt","r+")
        curnum=add.readline()
        curnum=int(curnum)
        curnum=curnum+1
        string=str(curnum)
        if(value==1):
            empno="CS"+str(curnum)+"RMS"
        elif(value==2):
            empno="CF"+str(curnum)+"RMS"
        elif(value==3):
            empno="WR"+str(curnum)+"RMS"
        elif(value==4):
            empno="OL"+str(curnum)+"RMS"
        add.seek(0)
        add.write(string)
        add.close()
        return empno

##################################################################
empname=input("Enter Employee Name:")
DOB=input("Enter date of birth:")
phno=int(input("Enter phone number:"))
email=input("Enter Email id:")
print("Choose employee type:")
init(convert=True)
cursor=0
choices=["1.Cashier","2.Chef","3.Waiter","4.Online"]
print("\n\n")
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
                empcat=1
                break
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
                empcat=2
                break
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
                empcat=3
                break
    elif(cursor==3):
            if key==87 or key==119:
                os.system('CLS')
                cursor=cursor-1
                ui.CLI()
                print("\n\n\n")
                choice()
            elif key==13:
                empcat=4
                break
empno=genEMPNO(empcat)
Empdetails(empname,DOB,phno,email,empno)

#Rishapp 24/11/2018
