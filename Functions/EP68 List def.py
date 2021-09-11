# List

def disList(item):  #กำหนดค่าลงไปได้เลย *กรณีที่ argument ที่ส่งมาไม่มีค่าที่ถูกส่งมา
    for i in range(len(item)) :
      print("ผลไม้ชิ้นที่ : ",i+1," =",item[i])

def disTuple(item):
    for i in range(len(item)) :
      print("ผักชิ้นที่ : ",i+1," =",item[i])


fruit=["mango","banana","Jackfriut"] #List
vetgetable=('แตงไท','แตงกวา','ชะอม') #Tuple

disList(fruit)
disTuple(vetgetable)
    
