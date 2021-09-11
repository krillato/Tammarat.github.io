# หาค่าเลขยกกำลัง
number=[1,2,3,4,5,6,7,8,9]
print(number)

#เขียนแบบปกติ
for i in range(len(number)) :
   number[i]=number[i]**2
print(number)

#เขียนแบบลดรูป
number=[i*i for i in number] # เอาค่าใน number แต่ละช่องเก็บไปที่ i  ==> แล้วก็ เอา i*i
print(number)