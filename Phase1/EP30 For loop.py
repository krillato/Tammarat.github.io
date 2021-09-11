# For loop ระบุจำนวนรอบได้เลย
#for i in range(start,stop,step) กำหนดรอบ
sum=0
for i in range(0,11,+1) :
    print("รอบที่ :",i+1)
    sum = sum + i
print("ผลบวกเลขตั้งแต่ 1 -10 : " , sum , "   Average : " , (sum/10))