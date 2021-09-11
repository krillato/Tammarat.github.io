# แบบ return

def add(a,b):  # แบบรับค่าเข้ามาและส่งค่ากลับไป
    return a+b

def show():  # ส่งค่ากลับออกมา แต่ไม่รับค่าเข้ามา
    return 500

def randomNum(x):  
    if len(x) < 3:
         return   #ออก
    if x == '100':
        print("ถูกหวย")
        return 1000
    else :
        print("ไม่ถูกหวย")
        return 0

#main

x=add(10,20)
print(x)

g=show()
print(g)

c=randomNum("10")
dept=300
#result=c-300   #หักลบหนี้
print("เงินรางวัล : ",c)
#print("เงินคงเหลือหลังจากหักลบหนี้ : ",result)