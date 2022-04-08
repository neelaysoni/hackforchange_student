#IMPORTING DIFFERENT MODULES 
import datetime #to display date and time 
import csv   #to use csv files
import pandas as pd #to use dataframe
import sys  #to use system exit
df=pd.read_csv(r"data.csv")
       
#SEARCH THE EXISITING ENTRY IN OUR CSV DATABASE
def login():
    f=pd.read_csv('data.csv')
    #taking username and password
    flag = 0
    while(flag == 0):
       with open('data.csv', 'r') as file:
          reader = csv.reader(file)
          print("-----------------------------------------------")
          print("Welcome to Student ID LOGIN Portal")
          x=datetime.datetime.now()
          print("Date\t: ",x.strftime("%x"))
          print("Time\t: ",x.strftime("%X"))
          print("-----------------------------------------------")
          id1=input("Enter Your User Id\t: ")
          pswd=input("Enter Your Password\t: ")
          for row in reader:
                a = row[10]
                b = row[11]
                if id1 == a and pswd == b:
                  print("Details For Entered Id and Password is :")
                  col=f.columns.values
                  for i in range(len(row)):
                    print(col[i]+"\t",":", "\t",row[i])
                    flag = 1
          if flag==0:
                print("!-----Wrong Input-----!")
    try:
        pass
    except IndexError:
        print("-----------------------")
    print("What Do You Want to Do Next : ")
    print("1 : SignIn/Delete/Anything")
    print("2 : Exit")
    a=int(input("Select 1 or 2 :"))
    if a==1:
        menu()
    else:
        exit()

#CREATE NEW USER
def signup():
    Fname=input("Enter First Name : ")
    Mname=input("Enter Middle Name : ")
    Lname=input("ENter Last Name : ")
    DOB=input("Enter YOur Date Of Birth(DD-MM-YY) :")
    BP=input("Enter Your Birth Place :")
    ADD=input("ENter Your Address : ")
    PIN=input("Enter Your PIN Code : ")
    MOB=input("Enter Your Mobile : ")
    mail=input("Enter Your Email :")
    Uname=input("Enter Your University Name : ")
    Fname.lower();Mname.lower();Lname.lower()
    Uid=mail[:-10]
    flag = 0
    
    while(flag == 1):
        Pswddd=input("Enter Password: ")
        CPswddd=input("Re-Enter Password: ")
        if Pswddd == CPswddd:
            flag = 1
            break
        else:
            print("Both Password Must Be Same")
    row1=[Fname,Mname,Lname,DOB,BP,ADD,PIN,MOB,mail,Uname,Uid,Pswddd]
    row=[row1]
    with open('data.csv', 'a') as csvfile:  
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerows(row)
    print("Please Note :")
    print("Your Generated User ID is : ",Uid)
    print("Your Entered Password is : ",Pswddd)
    print("THANKS FOR ENTERING YOUR INFO INTO OUR CLI")
    ("What Do You Want to Do Next : ")
    print("1 : SignIn/Delete/Anything")
    print("2 : Exit")
    a=int(input("Select 1 or 2 :"))
    if a==1:
        menu()
    else:
        exit()

#HELPDESK TO GUIDE
def help():
    print("Press 1 or Type Login to Log In (With The ID And Password You Have)")
    print("Press 2 or Type Sign Up (Just If Don't Have A Account)")
    print("Press 3 or Type FPSWD to Change to Password But Needs ID")
    print("Press 4 or Tpye DEL to Delete Your Current Account But You Will Need ID ,Password And Registered Phone Number Required")
    print("Press 5 or Type DBASE ")
    print("Press 6 or Tpye UPDATE to Update Account to make changes BUt ID and Password Required")
    print("Press 7 And Exit Directly")
    print("What Do You Want to Do Next : ")
    print("1 : SignIn/Delete/Anything")
    print("2 : Exit")
    a=int(input("Select 1 or 2 :"))
    if a==1:
        menu()
    else:
        exit()
        
#EXIT THE PROGRAM 
def exit():
    print("THANKS FOR USING OUR CLI PROGRAM")
    sys.exit()
    
#UPDATE EXISITING ACCOUNT 
def entrys(storedrow,Vals):
    name1=input("Entered Original Value :")
    name2=input("Enter Your New Value :")
    for i in storedrow:
        if name1==i:
            df[Vals]=df[Vals].replace(name1,name2)
            df.to_csv('data.csv',index=False)
            break
def change(a):
    #To Help Users To Select The Data They Want To Update
    #Number Refering The Update So Choose As Per Need
    print("--------------+------------------")
    print("1 : First Name")
    print("2 : Middle Name")
    print("3 : Last Name")
    print("4 : DOB Name")
    print("5 : Birth Place")
    print("6 : Address")
    print("7 : PIN Code")
    print("8 : Mobile Number")
    print("9 : E-Mail")
    print("10 : University Id")
    print("11 : Forget Password")
    sel2=int(input("Select What You Have To Change In Your Data Stored : "))
    #elif constuct to be more specific to our selection about update
    if sel2==1:
        entrys(a,'First Name ')
    elif sel2==2:
        entrys(a,'Middle Name ')
    elif sel2==3:
        entrys(a,'Last Name ')
    elif sel2==4:
        entrys(a,'DOB')
    elif sel2==5:
        entrys(a,'Birth Place')
    elif sel2==6:
        entrys(a,'Address')
    elif sel2==7:
        entrys(a,'Pin Code')
    elif sel2==8:
        entrys(a,'Mobile No.')
    elif sel2==9:
       entrys(a,'Email ID')
    elif sel2==10:
       entrys(a,'University Name')
def r1(rowstored):
    #stores the perticular entry you have entered Id And Pswd Of
    a = list(rowstored)
    change(a)
def update_acc():
    #checking Account Exists Or Not
    f=pd.read_csv('data.csv')
    #taking username and password
    flag = 0;slot=0
    while(flag == 0):
       with open('data.csv', 'r') as file:
          reader = csv.reader(file)
          print("-----------------------------------------------")
          print("Welcome to Student ID LOGIN Portal")
          x=datetime.datetime.now()
          print("Date\t: ",x.strftime("%x"))
          print("Time\t: ",x.strftime("%X"))
          print("-----------------------------------------------")
          id1=input("Enter Your User Id\t: ")
          pswd=input("Enter Your Password\t: ")
          for row in reader:
                a = row[10]
                b = row[11]
                if id1 == a and pswd == b:
                  r1(row)
                  print("Details For Entered Id and Password is :")
                  col=f.columns.values
                  for i in range(len(row)):
                    print(col[i]+"\t",":", "\t",row[i])
                    flag = 1;slot=1
          if flag==0:
                print("!-----Wrong Input-----!")

#DELETE ACCOUNT 
def delete_acc():
    #delete account completely and makes it row entirely NaN/Empty
    print("\nSystem In UnderMaintainance So Try After Some Time\n")
    
#MENU FUNCTION
def menu():
    #flag to choose option
    flag = 0
    while(flag != 7):
        
        #menu printing
        print("MAIN MENU\n")
        print("1 : Create New Account\n")
        print("2 : Search for existing account\n")
        print("3 : Delete existing account\n")
        print("4 : Update existing account\n")
        print("5 : Help Desk\n")
        print("6 : Exit Program\n")
        
        #if-else statements
        flag = input("Select Any One From Above : ")

        #Create New Account
        if (int(flag)==1 or flag.lower() == "signup"):
            signup()

        #Search for Existing Accounts
        elif (int(flag)==2 or flag.lower() == "login"):
            login()
        
        #Delete Existing Accounts
        elif (int(flag)==3 or flag.lower() == "delete"):
            delete_acc()

        #Update Existing Accounts
        elif (int(flag)==4 or flag.lower() == "update"):
            update_acc()

        #Help Desk
        elif (int(flag)==5 or flag.lower() == "help"):
            help()

        #Exit Program
        elif int(flag)==6 or flag.lower() == "exit":
            exit()

#DRIVER FUNCTIOM
def main():

    #Welcome statement
    print("***********************************************************************************************************")
    print("Welcome To Our Student ID CLI Program")
    
    #printing time
    date_time=datetime.datetime.now()
    print("Date\t: ",date_time.strftime("%x"))
    print("Time\t: ",date_time.strftime("%X"))

    #calling menu
    menu()
#calling driver function
main()