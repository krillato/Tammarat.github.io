'''
โครงสร้างควบคุม
1.แบบลำดับ
2.แบบเลือก
3.แบบทำซ้ำ
'''

age = int(input("Input you age :"))
name = "TeeTime"

# เงื่อนไข  if  elif  else  สามารถกำหไนดเงื่อนไข and , or

if age<=15 and age<18: 
    print("You kid")
elif age<=18:
    print("You แตกหนุ่ม")
else : 
    print("You วัยรุ่น")

#Ternary Operator ลดบรรทดเขียนย่อ
#"เงื่อนไขเป็นจริง" if expresstion else "เงื่อนไขอื่นๆ"
print("เด็ก") if age<=15 else print("ไม่เด็กนะครับ")
