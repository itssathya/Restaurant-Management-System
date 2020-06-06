from msvcrt import getch
from colorama import Fore,Back,Style,init
import os
import ui_base as ui
import dineInModule as dIM
import del_screen as ds
def choiceChoice(curnum,total,dataList):
    os.system('CLS')
    ui.CLI()
    init(convert=True)
    cursor=0
    choices=["[Dine In]","[Delivery]"]
    def choice():
        curform= Back.WHITE + Fore.BLACK + choices[cursor]+ Style.RESET_ALL
        print("Choose Order Mode: ")
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
                    tableno=input("Table No: ")
                    dIM.addToOrder(tableno,dataList,total,curnum)
                    input("Order Updated. DINE IN MODE. Press ENTER...")
                    os.system('admin_console.py')
        elif(cursor==1):
                if key==87 or key==119:
                    os.system('CLS')
                    cursor=cursor-1
                    ui.CLI()
                    choice()
                elif key==13:
                    ds.GetOrderNo(curnum,total)
