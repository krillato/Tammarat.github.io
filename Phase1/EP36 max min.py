# ค้นหาตัวเลขน้อยสุดมากสุด
i=1
max ,min = 0,0

while True :
  num = int(input("ป้อนตัวเลข :"))
  
  if num < 0 :
      print("จบโปรแกรม")
      break
  if num > max :
      max = num
  elif num < max :
      min = num
  print("ค่ามากสุด : ", max , "  ค่าน้อยสุด : ",min)
