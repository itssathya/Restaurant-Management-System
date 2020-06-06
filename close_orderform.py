#CloseOrderForm
import showFinal
import ui_base as ui
import os
os.system('CLS')
ui.CLI()
ractiveo=[]
activeo=[]
with open("activetables.txt",'r') as at:
    for line in at.readlines():
        activeo=line.split("|")
print("CURRENTLY ACTIVE ORDER(S)")
for i in activeo:
    if i not in ractiveo:
        ractiveo.append(i)
for i in ractiveo:
    print (i)
choice=input("Close Order: ")
if(choice=='b'):
    os.system('admin_console.py')
for i in ractiveo:
    if(i==choice):
        ractiveo.remove(i)
with open("activetables.txt",'w') as at:
    at.seek(0)
    for i in ractiveo:
        at.write(i+"|")
showFinal.showBill(choice)
