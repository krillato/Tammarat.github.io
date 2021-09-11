# ฟังก์ชันเรียกตัวมันเอง
"""
หาจุดวนซ้ำ
หาจุดสิ้นสุด ออกจาก function
ต้องมี Parameter

1-5 โดยไม่ใช้ loop
"""
def addnum(num):
    if num==5:
        return
    print("เลขที่ :",num) #0
    num+=1 #1
    addnum(num)
    
def sumation(sum):
    if sum == 1 :
     return sum
    else:  
     return sum+sumation(sum-1)  #sumation(sum-1) เป็นการเรียกทำงานในฟังก์ชันซ้ำ
    
    
    


#main()
addnum(0)
x=sumation(5)  #  5 4 3 2 1
print(x)
"""
การทำงานใน def sumation
5  => else => 5+sum(5-1)
4  => else => 5 + 4 + sum(4-1)
3  => else => 5 + 4 + 3 + sum(3-1)
2  => else => 5 + 4 + 3 + 2 +sum(2-1)
1 => if => return ออก
"""
