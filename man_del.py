#KITCHEN MODE
import os
import ui_base as ui
os.system('CLS')
ui.CLI()
def orderGet():
    global data
    for line in open("del_data.txt","r").readlines(): # Read the lines
        login_info = line.split('|')
        data.append(login_info)
def checkdel(choice):
    if (choice=='b'):
        os.system('admin_console.py')
    for i in data:
        if(i[5]==choice):
            return(data.index(i))
    input("ERROR.Press ENTER to continue...")
    os.system('admin_console.py')
def deleteIt(searchLine):
    with open("del_data.txt","r") as get:
        lines=get.readlines()
    with open("del_data.txt","w") as update:
        for line in lines:
            login_info = line.split('|')# Split on the space, and store the results in a list of two strings
            if(login_info!=searchLine):
                update.write(line)
              
from tabulate import tabulate
searchLine=''
data=[["CName",'Address',"Landmark","Area","Pincode","Order Number","COD"]]
orderGet()
print(tabulate(data))
choice=input("OUT FOR DELIVERY: ")
forCompare=checkdel(choice)
deleteIt(data[forCompare])
os.system('admin_console.py')
