#Show_Final_bill
import os
def showBill(tableno):
    current_dir=os.getcwd()
    total=0
    fooditem=[]
    final_dir=(os.path.join(current_dir, r'tableorder'))
    fileis=final_dir+"\\"+tableno+".txt"
    finalshow=open(fileis,'r')
    for line in finalshow.readlines():
        dataList=line.split("|")
        for item in dataList[0].split('~'):
            fooditem.append(item)
        total=total+float(dataList[1])
    print("ORDER SUMMARY")
    for i in fooditem:
        print(i)
    print("TOTAL: ",total)
    finalshow.close()
    os.remove(fileis)
    input("Order Successfully Closed. Press ENTER...")
    os.system('admin_console.py')
