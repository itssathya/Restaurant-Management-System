#Delivery Screen
import ui_base as ui
import os
def GetOrderNo(order,totalv):
    global orderno,total
    orderno=order
    total=totalv
    cname=input("Enter Customer Name: ")
    ad1=input("Address: ")
    ad2=input("Nearby Landmark: ")
    area=input("Area: ")
    try:
        pincode=int(input("Pincode"))
    except ValueError:
        input("Error! Enter Valid PINCODE. Press ENTER to retype...")
        os.system('del_screen.py')
    else:
        delupdate=open("del_data.txt",'a')
        delupdate.write(cname+"|"+ad1+"|Near "+ad2+"|"+area+"|"+str(pincode)+'|'+str(orderno)+'|'+str(total)+"|\n")
        delupdate.close()
        os.system('admin_console.py')
    
    
