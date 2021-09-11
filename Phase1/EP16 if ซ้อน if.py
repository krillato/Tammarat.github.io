# if ซ้อน if
# pass ผ่านไปก่อน
age=int(input("ใส่อายุ :"))


if age<=15:
    print("เด็ก ม ต้น")
    if age==13 : pass
    elif age==14 : print(" ม.2 งั้บ")
    elif age==15 : print(" ม.3 งั้บ")
    else : print("ประถม")
else :
    print("เด็ก ม ปลาย")
    if age==16 : print(" ม.4 งั้บ")
    elif age==17 : print(" ม.5 งั้บ")
    elif age==18 : print(" ม.6 งั้บ")

print("The end")