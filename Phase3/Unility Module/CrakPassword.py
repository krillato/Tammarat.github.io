# รหัส ATM = 556
# ทำการสุ่มรหัส crakPassword
import random

ATM_PASSWORD = "021"
result="" # สำหรับเก็บผลลัพธ์

# ("0123456789abcdefghijklmnopqrstuvwxyz")

while result != ATM_PASSWORD :
    result=""
    for letter in range(len(ATM_PASSWORD)) :
        list_number = random.choice("012")
        result="".join(list_number)+str(result)
        if (result==ATM_PASSWORD[0]) :
            result="".join(list_number)+str(result)
        print("SERACH ==> ",result)
print("CRACK PASSWORD IS : ",result)
