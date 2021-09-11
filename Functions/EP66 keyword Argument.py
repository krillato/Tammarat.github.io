# Keyword Argument
# Default Parameteter
def dis(fname,lname,city="กรุงเทพ"):  #กำหนดค่าลงไปได้เลย *กรณีที่ argument ที่ส่งมาไม่มีค่าที่ถูกส่งมา
    print("ชื่อ =",fname)
    print("นามสกุล =",lname)
    print("จังหวัด",city)
    
dis(fname="Time",lname="Chans",city="nonthaburi")  #ระบุ keyword ลงไปเลยป้องกันการผิดเพี้ยนของข้อมูล
dis(fname="mol",lname="Chans")  