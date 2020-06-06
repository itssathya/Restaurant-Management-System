#Dine in Module
import os
def addToOrder(tableno,dataList,total,curnum):
    current_dir=os.getcwd()
    final_dir=(os.path.join(current_dir, r'tableorder'))
    if not os.path.exists(final_dir):
        os.makedirs(final_dir)
    fileis=final_dir+"\\"+tableno+".txt"
    neword=open(fileis,'a+')
    for i in dataList:
        neword.write(i+"~")
    neword.write("|"+str(total)+"|"+str(curnum)+"|\n")
    neword.close()
    with open("activetables.txt",'a') as activate:
        activate.write(str(tableno)+"|")
