# Lambda function
"""
lambda argument : expression

"""

# ใช้งานฟังก์ชันแบบไม่ต้องสร้าง def

x = lambda name:name
sum = lambda x,y : x+y

print(x("TimeLand"))
print(sum(5,5))

# แบบใช้ def

def mypower(x):
    # x = ตัวเลข
    # a = เลขชี้กำลัง
    return lambda a : x**a

y=mypower(5)
result=y(2)  #5**2

print(result)
