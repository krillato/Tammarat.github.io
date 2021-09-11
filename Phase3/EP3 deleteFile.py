import os
try:
    if os.path.exists("score.txt"):
        os.remove("score.txt")
        print("ลบไฟล์แล้ว")
    else :
        print("ไม่พบไฟล์")
except Exception as e:
    print(e)
