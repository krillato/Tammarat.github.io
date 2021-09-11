# check ตัวอักษร

def chekString(mesage):
    result={"UPPER":0,"LOWER":0}
    for c in mesage:
        if c.isupper():
            result["UPPER"]+=1
        elif c.lower():
            result["LOWER"]+=1
        else :
            pass
    return result
        
mesage=input("ใส่ข้อความ :")
x = chekString(mesage)
print(x)