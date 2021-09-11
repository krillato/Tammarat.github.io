tup=(1,2,3,4,"TimeAndMix","มังคุด",True,53.5)  #Tuple  ใช้()
lis=[1,2,3,4,"TimeAndMix","มังคุด",True,53.5] #list   ใช้ []

# tup[0]="Max" ไม่สามารถเปลี่ยนข้อมูลที่กำหนดแล้วได้ใน Tuple
lis[0]="Love"

print(tup)
print(lis)

print(tup[1:4]) # ดึงข้อมูลออกมาแสดง

#แปลงข้อมูลจาก Tuple ==> List
print("ก่อนแก้ไข : ",tup)
lis=list(tup)
lis[0]="KKKKKKK"

tup=tuple(lis)
print("หัลงแก้ไข : ",tup)

for i in tup:
    print(i)

# เช็คว่า ตัวเลขนี้ อยู่ที index อะไร
x=tup.index(53.5)
print(x)

# การเรียงข้อมูล Tuple ต้องแปลงให้เป็น ==> list ก่อนจึงจะแปลงได้ และต้องเป็น str or int อย่างเดียว



