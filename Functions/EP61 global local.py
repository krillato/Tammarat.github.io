# Global variable / Local variable

def disNumber():
    x=10  # local
    print("มีค่า :",x," ใน")


#โปรแกรมหลัก
x=20  # global
disNumber()  # ใช้ค่าใน def
print("ค่า ",x," นอก")  # ใช้ค่าของ main

# global ทำงานในทุกส่วน
# x ด้านนอก
# local ทำงานเฉพาะส่วน
# x ด้านใน def