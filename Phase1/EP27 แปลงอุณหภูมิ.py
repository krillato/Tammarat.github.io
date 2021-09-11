#แปลงอุณหภูมิ  
'''
สูตร  C = (F-32)*(5/9)
     F = (C * (9/5)) +32
'''
temp=input("กรุณาใส่ อุณหูมิ และ หน่วยองศา :")

unit= temp[-1].upper()  # C,F
degree = int(temp[:-1]) #องศา


if unit=='C' :
    f = (degree) * (9/5) +32
    print("อุณหูมิ C : " , temp , " ==> " , "อุณหภูมิ F : " , f)
elif unit=='F' :
    f = (degree-32) * (5/59 )
    print("อุณหูมิ F : " , temp , " ==> " , "อุณหภูมิ C : " , f)
else :
    print("ผิดพลาด")