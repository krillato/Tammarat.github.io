# เขียนแบบ primitive
a=1
a1=2
a2=3
a3=4
# non primitive
number = []    #list ว่าง
number = [1,2,3,4,5,6,100,5,3,5] #list มีสมาชิก 1,2
all = ["Time","123","มิกซ์",50,True,-50]
#construtor
all = list(["Time","123","มิกซ์",50,True,-50])

#แสดงผล
print(all)

#เข้าถึงข้อมูล List
print(all[0:3], all[3]+all[5])

#การแก้ไขข้อมูล
# ชื่อตัวแปร [index] = "ข้อมูลที่แก้ไข"
all [1] ="Love"
print(all[0:3])
sum=0
for i in number :
    sum+=i
print(sum)

#ตรวจสอบว่ามีสมาชิกใน list
fan = ['time','mix','g','save']
if "saveg" in fan:
    print("เป็น")
else :
    print("ไม่เป็น")

# len ตรวจสอบจำนวนสมาชิก
print("จำนวนสมาชิก แฟน :",len(fan))

#หาขนาดสมาชิกทั้งหมด โดยใช้ for
for i in range(len(fan)) :
    print(fan[i])

# การเพิ่ม แทรก ข้อมูล
print("ก่อนเพิ่ม ข้อมูล :", fan)
fan.append("Sahaphap")
print("หลังเพิ่ม ข้อมูล :", fan)
#insert (index,สมาชิกใหม่)
fan.insert(2,"รัก")
print("หลังแทรก ข้อมูล :", fan)

#remove
fan.remove("รัก")
print("หลังเอาข้อมูลออก :", fan)
fan.pop()  #เอาข้อมูลที่เข้ามาล่าสุดออกไป
print("หลังPOPข้อมูลออก :", fan)
# del  เอาข้อมูลออกตาม index
del fan[3]
print("หลัง DEL ข้อมูลออก :", fan)
#เอาออกทั้งหมด
fan.clear()
print("หลัง เอา ข้อมูลออก ทั้งหมด:", fan ,"\n\n\n")

# คัดลอกข้อมูล
x=[]
print("ก่อนคัดลอกข้อมูล", x)
x=all.copy()
print("หลังคัดลอกข้อมูล", x)

#การรวมข้อมูล list เข้าด้วยกัน
allgroup= x+number
print("การรวมข้อมมูล", allgroup)

# การหาสมาชิกที่ซ้ำกันใน list
show=number.count(5)
print("แสดงตัวเลข 5 ใน list ใน number ว่าซ้ำกันกี่ตัว :", show)
