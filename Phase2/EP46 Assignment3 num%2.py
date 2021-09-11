# input และเรียงลำดับข้อมูลตัวเลข หา เลขคู่เลขคี่

num=[]
odd=[] # เลขคี่
even=[] # เลขคู่
while True :
    x=int(input("รับตัวเลข :"))
    if x < 0 :
        print("จบโปรแกรม")
        break
    
    if x%2==0 :
        even.append(x)
    if x%2!=0 :
        odd.append(x)
    num.append(x)

print("เลขทั้งหมด : ",num)
print("เลขคี่ทั้งหมด : ",odd)
print("เลขคู่ทั้งหมด : ",even)

