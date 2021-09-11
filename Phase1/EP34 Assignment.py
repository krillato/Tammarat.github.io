# เอาตัวเลขที่รับมาจากคีย์บอร์ด มารวมกัน
i=1
sum=0
while i<=5 :
    num=int(input("ป้อนตัวเลขตัวที่ : "))
    sum=sum+num
    i=i+1
else :
    print("ผลรวม : ", sum ,"   Average : ", (sum/5))