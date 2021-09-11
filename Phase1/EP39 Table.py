# ตารางหมาก ฮอส
'''
x = สีน้ำตาล
o = สีขาว

xoxo
oxox
xoxo
oxox

'''

square=int(input("ใส่ขนาดสี่เหลยี่มที่ต้องการ"))

for i in range(0,square) :
   
    for j in range(0,square) :
        
        if (j+i)%2 == 0 :
            print(end="x")
        else :
            print(end="o")

    print(" ")



    '''
3 * 3
row = 0 + column = 0    => 0 ได้ x
row = 0 + 1 column = 0  => 0 ได้ o
row = 0 + 2 column = 0  => 0 ได้ x

    '''