# input และเรียงลำดับข้อมูลตัวเลข

num=[]
while True :
    x=int(input("รับตัวเลข :"))
    if x < 0 :
        print("จบโปรแกรม")
        break
    num.append(x)

print ("ก่อนเรียง :",num)
num.sort()
print ("หลังเรียง น้อย ==> มาก :",num)
num.reverse()
print ("หลังเรียง มาก ==> น้อย :",num)
print("จบโปรแกรม")