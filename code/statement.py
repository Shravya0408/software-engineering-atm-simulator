from parsing import GetDict
import mysql.connector
from date import Date
Date=Date()
cred=GetDict()
conn=mysql.connector.connect(**cred)
cur=conn.cursor()

def Statement(acc_number="acc_number"):
    check="SELECT name,amount,acc_type,acc_number FROM details WHERE acc_number=%s"
    value=(acc_number,)
    cur.execute(check,value)
    res=cur.fetchall()
    print(Date)
    for i in res:
        print("Customer Name -"+i[0])
        print("Available Balance -"+i[1])
        print("Account -"+i[2])
        print("Account Number -"+i[3])
    return Statement
Statement()
    
