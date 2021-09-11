# ฟังก์ชัน เรียก ฟังก์ชัน

def equal(x,y,z):
    # ฟังก์ชันเรียกฟังชัน
   # a=compareMax(x,y) # ได้20มา
   # b=compareMax(a,z) # เอา a มา เปรียบเทียบ
    return compareMax(compareMax(x,y),z)  # เขียนแบบนี้ก็ได้

def compareMax(x,y) : 
    if x>y :
        return x
    else :
        return y


max = equal(-5,11,0)
print("ค่ามากสุด =", max)