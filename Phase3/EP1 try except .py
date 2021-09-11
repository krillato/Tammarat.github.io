#Exception
#ข้อผิดพลาดระหว่างการทำงานโปรแกรม และทำให้โปรแกรมหยุดทำงาน


"""
try:
    คำสั่งรันโปรแกรม
except:
    คำสั่งที่ทำงานตอนโปรแกรมมีข้อผิดพลาด
"""

while True:
    try:
       number1 = int(input("รับตัวเลข: "))  #ถ้ารับ นอกจากตัวเลข จะเกิด Exception
       number2 = int(input("รับตัวเลข: "))

       if number1 == 0 and number2 == 0: # ออกจาก loop
            break
       sum=number1/number2  #ถ้า / 0 จะ error
       print(sum)

       # 
       if number1 < 0 or number2 < 0:
           raise Exception("ไม่สามารถป้อนค่าติดลบได้")  #ส่งไปทำงานที่

    except Exception as e: # เป็นการระบุว่า เกิดข้อผิดพลาดอะไรแก้ยังไง (ให้โปรแกรมบอก)
        print(e)
        print("โปรแกรมมีข้อผิดพลาด")
    
    except ValueError:
        print("ต้องป้อนตัวเลขเท่านั้น")
    except ZeroDivisionError:
        print("ตัวที่ใช้หารต้องไม่ใช่ 0")
    except TypeError:
        print("ชนิดข้อมูล ไม่ตรงกัน")
#else : #กรณีไม่มีข้อผิดพลาด
    #print("จบโปรแกรม")
    finally : # กรณีพบข้อผิดพลาด ก็ไม่สนทำงานต่อไป  ** มักเอามาใช้กับโปรแกรมที่ต้องทำงานตลอดเวลา ใช้ดักข้อผิดพลาดเมื่อพบและทำงานต่อไป
        print("ทำงานต่อไป")
    
 


# กำหนดข้อผิดพลาดแบบชัดเจน
"""except ValueError:
    print("ต้องป้อนตัวเลขเท่านั้น")
except ZeroDivisionError:
    print("ตัวที่ใช้หารต้องไม่ใช่ 0")
except TypeError:
    print("ชนิดข้อมูล ไม่ตรงกัน")"""

# ValueError => ค่าผิดพลาด
# ZeroDivisionError
