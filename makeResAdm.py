#Delivery Screen
import ui_base as ui
import os
os.system('CLS')
ui.CLI()
cname=input("Enter Customer Name: ")
ad1=input("Time:")
delupdate=open("resData.txt",'a+')
delupdate.write(cname+"|"+ad1+"|"+"\n")
delupdate.close()
os.system('admin_console.py')
    
    
