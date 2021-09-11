#การค้นหาและนับจำนวนตัวอักษรในสมาชิก

message=["timei","vlove","yoiuu","xeron","liioni"]
result=[]

for i in message:
   result.append(i.count("i"))  # ตรวจสอบว่า มี i อยู่กี่ตัวในแต่ละคำภายใน list
print(result)