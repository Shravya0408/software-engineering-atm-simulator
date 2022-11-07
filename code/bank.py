import random
from parsing import GetDict
import mysql.connector
import math
cred=GetDict()
conn=mysql.connector.connect(**cred)
cur=conn.cursor()

#Creating a 8 digit random password.

def pin():
    digits = [i for i in range(0, 10)]
    random_str = ""
    for i in range(8):
        index = math.floor(random.random() * 10)
        random_str += str(digits[index])
    return random_str
pin()



#Creating a account number.

def randomNumber():
    num=[nums for nums in range(10)]
    random_gen=random.sample(num,8)
    random_acc=""
    for n in random_gen:
        random_acc=random_acc+str(n)
    return random_acc

def accountNumber():
    number=randomNumber()
    checkid="SELECT * FROM details"
    cur.execute(checkid)
    gen_id=cur.fetchall()
    acc_num=str(len(gen_id))+number
    return acc_num
accountNumber()
