#Registration Module for USER
import getpass
import pwd_encrypt
import ui_base as ui
from validate_email import validate_email
import os
import extn_encrypt as exencrypt
import check_exist as ce
os.system('CLS')
##############################__NEW REGISTRATION__#############################
def reguser(uname,pwd,cname,mobno,email):
    current_directory = os.getcwd()
    exencrypt.fileDecrypt(current_directory,'usracc')
    temp=pwd_encrypt.EncryptPass(pwd)
    file = open("usracc.txt","a")
    file.write(uname)
    file.write("|")
    file.write(str(temp))
    file.write("|\n")
    file.close()
    final_directory = os.path.join(current_directory, r'usraccs')
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
    newacc=open(final_directory+"\\"+uname+".txt",'w')
    newacc.write(cname)
    newacc.write("|")
    newacc.write(str(mobno))
    newacc.write("|")
    newacc.write(email)
    newacc.write("|")
    newacc.close()
    exencrypt.fileEncrypt(final_directory,uname)
    exencrypt.fileEncrypt(current_directory,'usracc')
    input("New User Successfully Registered! Press enter to continue...")
    os.system("login_module.py")
ui.CLI()
print("Registration Form\n\n")
custname=input("Customer Name: ")
try:
    mobno=int(input("Mobile Number: "))
    if(mobno<1000000000):
        raise ValueError("Please enter a valid mobile number. Press ENTER to continue...")
except ValueError as ve:
    print (ve)
    os.system('user_regmodule.py')
email=input("Email ID: ")
is_valid = validate_email(email)
uname=input("Username: ")
pwd=getpass.getpass("Enter Password: ")
pwdc=getpass.getpass("Confirm Password: ")
if(pwd==pwdc):
          if(is_valid==True):
              if(ce.CheckExist(uname,'usracc')== True):  
                    reguser(uname,pwd,custname,mobno,email)
              else:
                    input("Username already exists! Press enter to continue...")
                    os.system('user_regmodule.py')        
          else:
              input("Enter valid E-Mail Address! Press enter to continue...")
              os.system('user_regmodule.py')
else:
    input("Recheck password. Password and Confirm Password do not match! Press enter to continue...")
    os.system('user_regmodule.py')
