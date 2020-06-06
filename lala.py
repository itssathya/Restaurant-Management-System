def chooseDineMode():
    os.system('CLS')
    ui.CLI()
    init(convert=True)
    cursor=0
    choices=["[Dine in]","[Delivery]","[Online Pickup]"]
    def choice():
        curform= Back.WHITE + Fore.BLACK + choices[cursor]+ Style.RESET_ALL
        print("Choose Dine Mode: ")
        for i in range (len(choices)):
            if (i==cursor):
                print(curform)
                continue
            print(choices[i])
        choice()
        while(True):
            key = ord(getch())
            if(cursor==0):
                if key==83 or key==115:
                    os.system('CLS')
                    cursor=cursor+1
                    ui.CLI()
                    choice()
                elif key==13:
                    pass
            elif(cursor==1):
                if key==83 or key==115:
                    os.system('CLS')
                    cursor=cursor+1
                    ui.CLI()
                    choice()
                if key==87 or key==119:
                    os.system('CLS')
                    cursor=cursor-1
                    ui.CLI()
                    choice()
                elif key==13:
                    pass
            elif(cursor==2):
                if key==87 or key==119:
                    os.system('CLS')
                    cursor=cursor-1
                    ui.CLI()
                    choice()
                elif key==13:
                    pass
