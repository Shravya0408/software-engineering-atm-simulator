from parsing import GetDict
import mysql.connector
from bank import pin,accountNumber
from date import Date
from statement import Statement


Date=Date()

options=int(input("\t\t\t WELCOME TO ATM SIMULATOR\n\t\t\t     1.Create Account\n\t\t\t     2.Existing Customer\n"))

# Database connections Modify According to Developer Data
cred=GetDict()
conn=mysql.connector.connect(**cred)
cur=conn.cursor()


auto_pin=pin()
accountNumber=accountNumber()
statement=Statement()




try:
    #Creating Account
    def createAccount():
        if options==1:
            accounttype=int(input("\t\t\t     1.Current Account \n\t\t\t     2.Savings Account\n"))
            #Current Account
            if accounttype==1:
                print(Date)
                name=input("Enter Your Name:")
                email=input("Enter Your Email:")
                mobile=input("Enter Your Mobile number:")
                amount=int(input("Enter amount:"))
                account="Current"
                accountnum=accountNumber
                if amount>=500:
                    otp=auto_pin
                    # Create a table and insert into that particular table
                    add="INSERT INTO details(name,email,mobile,amount,acc_type,password,acc_number) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                    info=(name,email,mobile,amount,account,otp,accountnum)
                    cur.execute(add,info)
                    conn.commit()
                    print("\n\nThanks for creating your account. \nYour account number is "+accountnum+" \nYour password is "+otp)
                else:
                    print("Minimum amount is 500 to create your account.")
                                
            #Savings Account   
            elif accounttype==2:
                
                name=input("Enter your name:")
                email=input("Enter your email:")
                mobile=input("Enter your mobile number:")
                amount=int(input("Enter amount:"))
                account="Savings"
                #Automatic Generation of Account Number
                accountnum=accountNumber
                if amount>=500:
                    #Automatic Generation of Password
                    otp=auto_pin
                    add="INSERT INTO details(name,email,mobile,amount,acc_type,password,acc_number) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                    info=(name,email,mobile,amount,account,otp,accountnum)
                    cur.execute(add,info)
                    conn.commit()
                    print("\n\nThanks for creating your account. \nYour account number is "+accountnum+" \nYour password is "+otp)

                else:
                    print("Minimum amount is 500 to create your account.")

    createAccount()  

    # Function for validating the password     
    def checkCredentials(password):
        check="SELECT name FROM details WHERE password=%s"
        value=(password,)
        cur.execute(check,value)
        res=cur.fetchall()
        if len(res)==1:
            for i in res:
                for name in i:
                    print("\t\t\tWELCOME "+name+" TO ATM SIMULATOR")
            return 1
        else:
            return 0

    def checkAccnum(acc_num):
        check="SELECT name FROM details WHERE acc_number=%s"
        value=(acc_num,)
        cur.execute(check,value)
        res=cur.fetchall()
        if len(res)==1:
            return 1
        else:
            return 0
            
    #Validating existing customer
    def existingCustomer():
        if options==2:
            acc_num=input("Enter your account number:")
            password=input("Enter your password:")
            op=checkCredentials(password)
            op1=checkAccnum(acc_num)
            if( op==1 & op1==1):
                index=int(input("\t\t\t     1.Account Statement \n\t\t\t     2.Withdraw \n\t\t\t     3.Deposit \n\t\t\t     4.Change Password \n\t\t\t     5.Logout \n"))
                #Account Statement
                if index==1:
                    statement(acc_num)
                #Withdraw
                elif index==2:
                    print(Date)
                    debit=int(input("Enter amount:"))
                    def Withdraw():
                        check="SELECT amount FROM details WHERE acc_number=%s"
                        value=(acc_num,)
                        cur.execute(check,value)
                        res=cur.fetchall()
                        available=""
                        for amount in res:
                            available=available+amount[0]
                        if debit>int(available):
                            print("Insufficient amount")
                        else:
                            remaining=int(available)-debit
                            update = "UPDATE details SET amount =%s WHERE acc_number =%s"
                            val=(remaining,acc_num)
                            cur.execute(update,val)
                            conn.commit()
                            print("Please collect your cash")
                            print("Available balance "+str(remaining))                    
                    Withdraw()
                #Deposit
                elif index==3:
                    print(Date)
                    credit=int(input("Enter amount:"))
                    def Deposit():
                        check="SELECT amount FROM details WHERE acc_number=%s"
                        value=(acc_num,)
                        cur.execute(check,value)
                        res=cur.fetchall()
                        available=""
                        for amount in res:
                            available=available+amount[0]
                        total_amount=int(available)+credit
                        update = "UPDATE details SET amount =%s WHERE acc_number =%s"
                        val=(total_amount,acc_num)
                        cur.execute(update,val)
                        conn.commit()
                        print("Deposited successfully")
                        print("Available balance "+str(total_amount))
                    Deposit()
                #For modifying password
                elif index==4:
                    def modify_password():
                        check="SELECT password FROM details WHERE acc_number=%s"
                        value=(acc_num,)
                        cur.execute(check,value)
                        res=cur.fetchall()
                        current_password=""
                        for password in res:
                            current_password=current_password+password[0]
                        new_password=input("Enter new password:")
                        if(len(new_password)<=8):
                            update = "UPDATE details SET password =%s WHERE password =%s"
                            val=(new_password,current_password)
                            cur.execute(update,val)
                            conn.commit()
                            print("Password is changed successfully")
                            print("\nYour new password is "+new_password)
                        else:
                            print("Password length exceeds 8 characters")

                    modify_password()
                #Logout
                elif index==5:
                    exit()

            else:
                print("Check your login credentials")
    existingCustomer()
except Exception as e:
    print(e)
