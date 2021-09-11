# การวนซ้ำ While Loop  ทำงานต่อเมื่อเงื่อนไขเป็นจริง
'''
python จะมี while , for

while   expreesion :
        statement
'''
i = 1
sum=0
while i<=100 :  # บวกเลข1-100
    sum = sum + i
    i=i+1
print("ผลบวกเลขตั้งแต่ 1 -100 : " , sum , "   Average : " , (sum/100))
