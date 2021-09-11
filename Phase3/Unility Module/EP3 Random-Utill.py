import random

  
#  x = random.random()  ==>  สุ่มตัวเลขทศนิยม 0.0 - 1.0
#  x = random.uniform(5,10)  ==>  สุ่มตัวเลขทศนิยม 5.0 - 10.0
#  x = random.randrange(start, stop, step)  ==> สุ่มเลขจำนวนเต็ม   
# random.randrange(1,10,2) สุ่มเฉพาะเลขขี้ 1 3 5 7 9
#  x = random.randint(1,5)   ==> สุ่มค่าตั้งแต่ 1 ถึง 5 เลย

items=[1,2,3,4,5,"A","B"]
# x = random.choice(items) กรณีกำหนดตัวที่อยากสุ่มเอง
# random.shuffle(items)  ==> การสลับค่าทั้งหมดใน list สุ่มเปลี่ยนตำแหน่ง

for i in range(10):
    random.shuffle(items)
    x = random.choice("0123456789")
    #print(items)
    print(x)
