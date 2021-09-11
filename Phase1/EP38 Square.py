#สร้างสี่เหลี่ยมจัตตุรัส
'''
xxx
x x
xxx
'''
square=int(input("ใส่ขนาดสี่เหลยี่มที่ต้องการ"))

for i in range(0,square) :
    for j in range(0,square) :
        if i == 0 or i == square-1 or j == 0 or j== square-1:
          print(end="x")
        else :
            print(" ",end=(''))
    print(" ")