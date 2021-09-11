# Module Date Time
import datetime

result = datetime.datetime.now()   #ดึงวันเวลาปัจจุบัน
#print(result)   # เอาเฉพาะส่วน  .year  .month .day
#print(result.month) 
#print(result.day) 

#newdate = datetime.datetime(2020,10,2,13) # yyyy,mm,dd  แบบระบุวันเอง
#print(newdate)

#รูปแบบแสดงผล
print("รูปแบบเริ่มต้น  ==> ",result) 
print("รูปแบบใหม่    ==> ",result.strftime("%x"))  #==> 05/08/21 วัน
print("รูปแบบใหม่    ==> ",result.strftime("%X"))  #==> 13:17:02 เวลา
print("รูปแบบใหม่    ==> ",result.strftime("%c"))  #==> Sat May  8 13:16:03 2021 
 
 #เวลา
print("รูปแบบใหม่    ==> ",result.strftime("%H : %M : %S %p"))   #==>  13 เวลา(ชั่วโมง)  , 19 นาที , 37 วินาที , AM or PM

# วันที่เท่าไหร่ใน 365 วัน  1 - 365
print("วันที่ ==> ",result.strftime("%j"))  # วันที่ ==>  128 

#date 
print("วันที่ ==> ",result.strftime("%a")) # วันที่ ==>  Sat (แบบสั้น)
print("วันที่ ==> ",result.strftime("%A")) # วันที่ ==>  Saturday (แบบยาว)
print("วันที่ ==> ",result.strftime("%w")," ของสัปดาห์") # วันที่ ==>  6  ของสัปดาห์
print("วันที่ ==> ",result.strftime("%d")) # วันที่ ของเดือน
print("วันที่ ==> ",result.strftime("%b")) # เดือน ย่อ
print("วันที่ ==> ",result.strftime("%B")) # เดือนเต็ม

# ว/ด/ป
print("วันที่ ==> ",result.strftime("%A  ที่  %d  เดือน  %B  ปี  %Y")) # วันที่ ==>  Saturday  ที่  08  เดือน  May  ปี  2021