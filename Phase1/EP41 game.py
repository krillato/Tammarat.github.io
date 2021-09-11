# เกมทายลูกเต๋า
# 1 2 3 4 5 6
# ฟังก์ชันการสุ่ม random
import random

myran = random.randrange(1,6)  #สุ่มตัวเลขตั้งแต่ 1 - 6
"""round=0
while True:
    num = int(input("ใส่ตัวเลข :"))
    correct = (num==myran) # true / false
    round+=1
    if correct :
        print("เก่งมากทายถูกจ้า")
        break
    if not correct:
        if num < myran:
            print("ตัวเลขที่สุ่มมีค่าน้อยกว่า")
        if num > myran:
            print("ตัวเลขที่สุ่มมีค่ามากกว่า")
    else :
        print("ทายผิดน่ะจ้าา")
    if num < 0 or round==3 :
        print("ออกจากโปรแกรม")
        break
if not correct:
    print("เฉลย :", myran)
    print("เสียใจด้วยนะ")"""

a = random.randrange(0,9)
b = random.randrange(0,9)
c = random.randrange(0,9)
d = random.randrange(0,9)
e = random.randrange(0,9)
f = random.randrange(0,9)
print(a,b,c,d,e,f)