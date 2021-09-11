
# min( , , ,) , max(, , ,) , abs() absolute
# pow(x,y)

import math
# math.sqrt(64) ==> squarroot
result = math.sqrt(64)

score = math.floor(80.4)  # math.floor(float) ==> ปัดเศษลง
score1 = math.ceil(80.4)  # math.ceil(float) ==> ปัดเศษขึ้น

# ค่าตรีโกณมิติ
convert = math.radians(90)   # หาค่ารัศมีเพราะหน่วยเป็น radians
x = math.sin(convert)        # หาค่า sin , cos tan ได้  ==> ทไให้เป็น เรเดียน ก่อน ค่อยหา ตรีโกณ
#print(x)

#หาระยะห่างระหว่าง point
point1 = [5,4]
point2 = [5,13]
d = math.dist(point1,point2)
#print(d)

# log
lo = math.log2(32)
print(lo)