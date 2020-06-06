#Adding Item To ItemList
import ui_base as ui
import check_exist as ce
import os
os.system('CLS')
ui.CLI()
def ItemAddDB(prodcode,itemname,itemprice):
    with open("itemdata.txt","a+") as itupdate:
        itupdate.write(prodcode)
        itupdate.write("|")
        itupdate.write(itemname)
        itupdate.write("|")
        itupdate.write(str(itemprice))
        itupdate.write("|\n")
    input("Item added successfully. Press ENTER to continue...")
    os.system('admin_console.py')
#------------------------------------------------------------------------
print("ADD ITEM")
prodcode=input("Enter desired product code: ")
itemname=input("Enter Item Name: ")
itemprice=float(input("Enter the price of the item: "))
if(ce.CheckExist(prodcode,"itemdata")== False):
    input("Product Code already exists. Press ENTER to try again.")
    os.system("item_add.py")
else:
    ItemAddDB(prodcode,itemname,itemprice)
    
