# ค้าหาเบอร์โทรศัพท์
data={"191":"ตำรวจ","1112":"ไก่ทอด","1150":"พิซซ่า"}

def search(mesage):
    for key , value in data.items():
        if key==mesage:
            print("เบอร์ติดต่อ = ",value)
            return
        else :
            print("ไม่มีข้อมูล")
            return

mesage = input("ใส่เบอร์ ")
search(mesage)
