import datetime
def Date():
    x = datetime.datetime.now()
    date=x.strftime("%x")
    time=x.strftime("%X")
    res=date+"\t\t\t\t\t\t\t"+time
    return res
Date()
