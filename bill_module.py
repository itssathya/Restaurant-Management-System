#Billing MODULE
import ui_base as ui
import os
from tabulate import tabulate
import datetime
from colorama import Fore,Back,Style,init
from msvcrt import getch
import orderchoice as oc
now = datetime.datetime.now()
os.system('CLS')
def itemData():
    def orderGet():
        data=[["Item ID","Name","MRP"]]
        for line in open("itemdata.txt","r").readlines(): # Read the lines
            login_info = line.split('|')
            data.append(login_info)
        return data
    data=orderGet()
    print(tabulate(data))
    input("Press Enter to continue billing...")
    billItem()
def totalBill():
    global totord,total
    print("\n\nTOTAL = ",total)
    add=open("orderno.txt","r+")
    curnum=add.readline()
    curnum=int(curnum)
    string=str(curnum+1)
    add.seek(0)
    add.write(string)
    add.close()
    uporder=open("current_orders.txt","a+")
    uporder.write(str(curnum))
    uporder.write("|")
    uporder.write(str(now.strftime('%Y-%m-%d %H:%M:%S')))
    uporder.write("|")
    for i in totord:
        uporder.write(i)
        uporder.write("|")
    uporder.write("\n")
    uporder.close()
    oc.choiceChoice(curnum,total,totord)
    input("Order Generated. Press ENTER to continue...")
    os.system('admin_console.py')
def itemtest(itemcode):
    for line in open("itemdata.txt","r").readlines(): # Read the lines
        login_info = line.split('|')# Split on the space, and store the results in a list of two strings
        if(itemcode==login_info[0]):
            return login_info
    return False
def billItem():
    global total,totord,menu
    os.system('CLS')
    ui.CLI()
    print(tabulate(menu))
    itemcode=input('CODE: ')
    if(itemcode=='i'):
        itemData()
    if(itemcode=='b'):
        os.system('admin_console.py')
    if(itemcode != "end"):
        qty=int(input('QTY: '))
        if(itemtest(itemcode)==False):
            input("Invalid Code! Press ENTER to continue...")
            billItem()
        else:
            curItem=[]
            prodData=itemtest(itemcode)
            totord.append(prodData[1]+" x"+str(qty))
            amount=float(prodData[2])
            prodData[3]=qty
            prodData.append(qty*amount)
            total=total+(qty*amount)
            menu.append(prodData)
            billItem()
    else:
        totalBill()

total=0;totord=[]
menu=[["Item Code","Item Name","MRP","Qty","Amount"]]
billItem()
