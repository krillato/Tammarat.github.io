import os

try:
    fw = open("Score.txt","r",encoding="utf-8")
    fr = open("Grade.txt","w",encoding="utf-8")
  #  print("สร้างไฟล์เรียบร้อย")

   # while True:
   #     stuid = input("ป้อนข้อมูลรหัสนักเรียน :")
    #    if stuid == "exit":
     #       break
      #  score = input("คะแนน: ")
#
 #       fw.writelines(stuid+"\t"+score+"\n")  #เอาข้อมูลที่รับมาไปใส่ใน txt
 
    grade=None
    for line in fw.readlines():
        score=line[-3:].strip() # ลบช่องว่าง
        stuid=line[:-4].strip() 

        
        score=int(score)
        if score >= 80:
            grade="A"
        elif score >=70 and score<80:
            grade="B"
        elif score >=50 and score<=69:
            grade="C"
        else :
            grade="F"

        print("รหัสนักเรียน :",stuid , "  ได้คะแนน => ",score, "  GRADE : ",grade)
        fr.writelines(stuid+"\t"+str(score)+"\t"+grade+"\n") #เขียนในไฟล์ใหม่
    fw.close()
    fr.close()

except Exception as e:
    print(e)