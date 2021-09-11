#เขียนโปรแกรมเปรียบเทียบ ตัวเลข 2 ตัว

numA = float(input("input you first number :"))
numB = float(input("input you last number :"))

if numA > numB : print("ตัวเลขแรก  "+ str(numA) + "  <มากกว่า>  "+ str(numB)+ "  ตัวเลขสุดท้าย")
else : print("ตัวเลขแรก  "+ str(numA) + "  <น้อยกว่า>  "+ str(numB)+ "  ตัวเลขสุดท้าย")