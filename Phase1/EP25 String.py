name='TeeTime'  # index => 0

#แสดงเฉพาะตำแหน่งที่ต้องการ
print(name[3])
print(name[0:3])  #เอาตำแหน่งแรก ถึง ตำแหน่งสุดท้าย - 1
print(name[:3])   #เอาตั้งแต่ตำแหน่งแรกถึงตำแหน่งที่ 3-1
print(name[3:])   #เอาตั้งแต่ตำแหน่งที่3เป็นต้นไป
print(name[-2])   #เอาตำแหน่งที่ 2 นับจากตัวสุดท้าย (ตัวสุดท้ายเริ่มนับจาก1)
print(name[-2:])  #เอาตั้งแต่ตำแหน่งที่ 2 นับจากตัวสุดท้าย (ตัวสุดท้ายเริ่มนับจาก1)

print(len(name))  # นับความยาว

# strip การลบช่องว่างของตำแหน่งซ้ายและขวา
na = " LoveMix "
print(na) 
print(len(na))
na = na.strip()
print(na) 
print(len(na))

# ลบช่องว่างเฉพาะด้าน ใดด้านหนึ่ง  lstrip => ด้านซ้าย
nax = " LoveMixLo "
nax = nax.lstrip()
print(nax) 
print(len(nax))
nax = nax.rstrip()
print(nax) 
print(len(nax))

#ทำให้ตัวอักษรเป็นพิมพ์ใหญ่ หรือ เล็ก  .lower()  .upper()  
print(na.lower())
print(na.upper())

#แปลงข้อความ ทำให้ตัวแรกเป็นตัวพิมพ์ใหญ่ .capitalize()
some='timemix'
print(some.capitalize())

# การแทนที่คำ  .replace("ข้อความใหม่","ข้อความที่ต้องการแทนที่",จุดที่พบ(1ข้อความอาจจะเจอมากกว่า1จุด))
print(nax.replace("Lo","Time",1))

# ตรวจสอบว่ามีข้อความอยู่ในประโยคหรือไม่  in , not in
x = "Mix" in nax
print(x)

#การต่อ string  ด้วย {}
fname = "Time"
lname = "Sahaphap"
age = "21"

text="ชื่อ :{}\tชื่อแฟน :{} \tอายุ :{}"  # ระบุเลขตำแหน่งได้ {0}

print(text.format(fname,lname,age))

#นับจำนวนคำที่มีในประโยค  count
group="ชาวด้อมของน้อนมิกซ์ เชียร์น้อนมิกซ์ สรุป น้อนมิกซ์ชอบก่อนหรือพี่เอิร์ทชอบก่อน"
print(group.count("น้อนมิกซ์"))

#เช็คคำขึ้นต้น
name = "นายธรรมรัต"
print(name.startswith("นาย"))
