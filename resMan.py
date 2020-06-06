#KITCHEN MODE
import os
import ui_base as ui
os.system('CLS')
ui.CLI()
def orderGet():
    global data
    for line in open("resData.txt","r").readlines(): # Read the lines
        login_info = line.split('|')
        data.append(login_info)
def checkdel(choice):
    if (choice=='b'):
        os.system('admin_console.py')
    for i in data:
        if(i[0]==choice):
            return(data.index(i))
    input("ERROR.Press ENTER to continue...")
    os.system('admin_console.pu')
def deleteIt(searchLine):
    with open("resData.txt","r") as get:
        lines=get.readlines()
    with open("resData.txt","w") as update:
        for line in lines:
            login_info = line.split('|')# Split on the space, and store the results in a list of two strings
            if(login_info!=searchLine):
                update.write(line)
              
from tabulate import tabulate
searchLine=''
data=[["CName","Time"]]
orderGet()
print(tabulate(data))
choice=input("Close Reservation [ENTER CNAME]: ")
forCompare=checkdel(choice)
deleteIt(data[forCompare])
os.system('admin_console.py')
