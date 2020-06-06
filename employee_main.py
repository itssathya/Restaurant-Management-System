#Employee Main Screen
from tabulate import tabulate
import ui_base as ui
from colorama import Fore,Back,Style,init
from msvcrt import getch
import os
os.system('CLS')
ui.CLI()
dataList=[]
print("\nEmployee Data")
titlelist=[["Employee Name","DOB","Contact No.","E-Mail","EID"],['-','-','-','-','-']]
empData=open("employee_record.txt",'r')
for line in empData.readlines():
    datais=line.split("|")
    titlelist.append(datais)
print(tabulate(titlelist))
print("\n\n")
def choiceChoice():
    os.system('CLS')
    ui.CLI()
    init(convert=True)
    cursor=0
    choices=["[Add Employee]","[Back]"]
    def choice():
        print(tabulate(titlelist))
        curform= Back.WHITE + Fore.BLACK + choices[cursor]+ Style.RESET_ALL
        print("OPTIONS:")
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
                    choice()
                elif key==13:
                    os.system('emp_add.py')
        elif(cursor==1):
                if key==87 or key==119:
                    os.system('CLS')
                    cursor=cursor-1
                    ui.CLI()
                    choice()
                elif key==13:
                    os.system('admin_console.py')
choiceChoice()

