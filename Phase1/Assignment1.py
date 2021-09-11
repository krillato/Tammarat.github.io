#โปรแกรมคำนวณค่า BMI (ดัชนีมวลกาย)
# BMI = นน(kg) / high ^2 (m)

weight = float(input("please input your weight (kg): "))
high = float(input("please input your high (cm): "))

#process
#cm => m
high = high / 100
bmi = weight / (high**2)
print("BMI Your Is : ",bmi)