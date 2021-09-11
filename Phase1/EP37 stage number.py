#ตัวเลขขั้นบันได
'''
input 5
1
12
123
1234
12345
'''
k=0
num = int(input("ใส่ตัวเลขขั้นบันไดที่ต้องการ"))

for row in range(1,num+1) :
    for column in range(1,row+1) :
        print(column,end=' ')
    print(" ")
