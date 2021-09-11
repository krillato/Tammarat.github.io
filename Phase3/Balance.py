# โปรแกรมบัญชีธนาคาร

#data
account={'Time':5000 , 'Mix':0}

def getBalance():
    
    print("บอดเงินคงเหลือ",account)

def deposit(money):
    if money<=0:
        raise Exception ("ค่าตัวเลขต้องเป็นบวกเท่านั้น")
    print("ฝากเงินเข้าบัญชี :",money)
    account['Time']+=money

def withdraw(money):
    if not type(money) is int and not type(money) is float:   # ที่รับเข้ามาต้องเป็น int 
        raise Exception("ต้องป้อนตัวเลขเท่านั้น")
    if money<=0:
        raise Exception ("ค่าตัวเลขต้องเป็นบวกเท่านั้น")
    if money>account['Time']:
        raise Exception ("ยอดเงินในบัญชีไม่พอ")
    print("ถอนเงินจากบัญชี :",money)
    account['Time']-=money

def transfer(money):
    if money<=0:
        raise Exception ("ค่าตัวเลขต้องเป็นบวกเท่านั้น")
    if money>account['Time']:
        raise Exception ("ยอดเงินในบัญชีไม่พอ")
    print("ทำการโอนเงิน :",money)
    account['Time']-=money
    account['Mix']+=money

try:
    getBalance()
    withdraw(6000)
    getBalance()
except Exception as e:
    print(e)

