# เอาความสามารถของทุกตัวมารวมกันหมด

#dictionary => key(การเข้าถึงข้อมูล) , value(ค่าของข้อมูล)
#list, tuple => index , value 

#การสร้าง dict
#ชื่อตัวแปร = {key:value , key:value , key:value}
colors={"red":"สีแดง" ,"yellow":"สีเหลือง" ,"green":"สีเขียว" }
city={"bangkok":"กรุงเทพ"}
room={"ไทม์":210 , "มิกซ์":211 , 212:"ทิม"}
print(colors["green"])  #ต้องระบุ key เพื่อเรียกใช้ value
print(city["bangkok"]) 
print(room[212]) 

animals = dict(cat="แมว",brid="นก",lion="สิงโต")
print(animals["cat"])

animals.update(Time="Mix")
print(animals)
#แสดงตัวตัวใน dict
for i,o in animals.items() : #animals.values() หรือ animals.keys()
    print("Key = ",i,"  Value = ",o)

#เอาสมาชิกออก
animals.popitem() # เอาตัวที่อยู่หลังสุดออก
animals.pop("cat") # เอาตัวที่ระบุ key ออก
animals.clear()   # เอาออกทั้งหมด

# แบบใส่หลายค่า

market={
    "ร้านไทม์":{
        "name":"ไทม์น่ารัก",
        "menu":"ผัดกระเพรา",
        "location":"ที่ไหนก็ได้โตแล้ว"
    },
    "ร้านอร่อย":{
        "name":"อ้ามมน่ารัก",
        "menu":"ข้าวราดแกง",
        "location":"สวรรค์"
    }
}
print(market)