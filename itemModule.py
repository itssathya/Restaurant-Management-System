#KITCHEN MODE
import os
import ui_base as ui
from tabulate import tabulate
os.system('CLS')
ui.CLI()
def itemData():
    def orderGet():
        data=[["Item ID","Name","MRP"]]
        for line in open("itemdata.txt","r").readlines(): # Read the lines
            login_info = line.split('|')
            data.append(login_info)
        return data
    data=orderGet()
    print(tabulate(data))
    input("PRESS ENTER TO GO BACK")
    os.system('admin_console.py')
itemData()
