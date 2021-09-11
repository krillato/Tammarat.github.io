#union รวมทั้งหมด
fruitA={"มะม่วง","ทุเรียน","มังคุด","ส้ม",'กล้วย'}
fruitB={"สตอ","กีวี","กล้วย","เย็น",'ทุเรียน'}

allfruit=fruitA.union(fruitB)
#fruitA.update(fruitB) เขียนแบนี้ก็ได้
print(allfruit)

# เอาตัวที่ไม่เหมือนกัน
fruitC=fruitA.difference(fruitB)
print(fruitC)

#เอาตัวที่ เหมือนกัน
fruitC=fruitA.intersection(fruitB)
print(fruitC)

#subset  อยู่ใน subset ไหม
fish={'ปลานิล','ปลาดุก','ปลาหมอ','ปลาช่อน'}
f={'ปลานิล','ปลาจิก'}
y={'ปลาดุก','ปลาช่อน'}
print(f.issubset(fish))  # ไม่อยู่ เพราะไม่มี ปลาจิก ใน set ของ fish
print(fish.issuperset(y)) # เช็คว่า y เป็น set  หลัก ของ fish หรือป่าว

# min,max
num={6,3,15,4,32,652,65,54,87,21,0,13,-5,0.1,365,652,111,-56}
print(min(num),max(num))