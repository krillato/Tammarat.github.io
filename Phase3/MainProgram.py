# โปรแกรมหลัก
#เรียกใช้ โมดูล calculate ที่สร้างเอาไว้ และ กำหนดชื่อเล่น คือ c
import Mypackage.calculate as c   # ชื่อโฟลเดอร์ที่เก็บ.ชื่อโมดุล
import Mypackage.weather as w

# หยิบเฉพาะ ฟังก์ชันในโมดูลมา 
from Mypackage.calculate import addition
addition(10,5,10)
#

c.addition(5,10,20)  # รเียกใช้ โดย เรียกโมดูล.ชื่อฟังก์ชันที่ต้องการใช้
c.sub(50,25)
print(c.PI)   #ดึงต่าที่ประกาศไว้ใน โมดูล

result = w.city["ชลบุรี"]
print(result)

w.getweather()

