#โปรแกรมคำนวณค่า BMI (ดัชนีมวลกาย)
# BMI = นน(kg) / high ^2 (m)

weight = float(input("please input your weight (kg): "))
high = float(input("please input your high (cm): "))/100

#process
bmi = weight / (high**2)
print("BMI Your Is : ",bmi)

'''

<18  ต่ำกว่าเกณฑ์
18.5 - 22.9  = สมส่วน
23.0 - 24.9  = น้ำหนักเกิน
25.0 - 29.9  = โรคอ้วนระดับ 1
>30 = โรคอ้วนระดับอันตราย

'''
if bmi<18.5 :
    print("ค่า BMI ของคุณ < ต่ำกว่าเกณฑ์ > ")

elif bmi<22.9 :
    print("ค่า BMI ของคุณ < สมส่วน> ")

elif bmi<24.9 :
    print("ค่า BMI ของคุณ < น้ำหนักเกิน> ")

elif bmi<30 :
    print("ค่า BMI ของคุณ < โรคอ้วนระดับ 1 > ")

else :
    print("ค่า BMI ของคุณ < โรคอ้วนระดับอันตราย > ")

