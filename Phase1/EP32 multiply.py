# user ใส่ ตัวเลขว่า ต้องการดูสูตรคูณแม่อะไร

'''
math = int(input("ใส่แม่ที่ต้องการ :"))
for i in range(1,13,1) :
    print(math , " x " , i , " = " , (math*i))

k=1
while k<=12 :
    print(math , " x " , k , " = " , (math*k))
    k=k+1
'''

start=int(input("ใส่แม่เริ่มต้น : "))
stop=int(input("ใส่แม่สุดท้าย : "))

for i in range(start,stop+1,1) :
    print("แม่ ",i)
    for k in range(1,13,1) :
        print(i , " x " , k , " = " , (i*k))
