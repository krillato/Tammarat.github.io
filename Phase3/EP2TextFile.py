
#open("ชื่อไฟล์","โหมด","เข้ารหัส")
# โหมด การทำงาน อ่าน(r) เขียน(w) เพิ่ม(a)  ไฟล์เปล่า (x)  
# การเข้ารหัสต่างภาษา
# อ่าน open(r"C:\Users\lenovo\Desktop\python\Phase3\score.txt",encoding="utf-8")
# เขียน f = open("score.txt","w",encoding="utf-8")
#f.write("i am try\n")
#f.writelines("สวัสดีที่รัก  iam ")

import os  #ใช้ในการดำเนินการตำแหน่งของไฟล์

try:
    f = open("score.txt","r",encoding="utf-8")  #or  C:\\Users\\lenovo\\Desktop\\python\\Phase3\\file.txt
    line = f.readlines()

    for i in line: # แสดงทีละบรรทัด
        print(i)
    
    name=input("ใส่ชื่อเลยโว้ย : ")

    fw = open("score.txt","a",encoding="utf-8") 
    fw.writelines("\n"+name)
    f.close()
    fw.close()

except FileNotFoundError:
    print("หาไฟล์ไม่เจอจ้าา")