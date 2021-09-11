# use function to fine number add,odd

def dis(num) :
    if num%2==0:
        print("เลขคู่")
    else :
        print("เลขคี่")

#main

while True :
    num = int(input("รับตัวเลข  "))
    dis(num)
    if num < 0 :
        print("จบโปรแกรม")
        break