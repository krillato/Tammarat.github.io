#แลกเงินและหาจำนวนแบงค์
num = int(input("input you amount : "))
if num >= 1000 : 
    print("แลกเงิน แบงค์ 1000 => ", num//1000 , "  ใบ")
    num %= 1000
    print(num)

if num >= 500 :  
    print("แลกเงิน แบงค์ 500 => ", num//500,"  ใบ")
    num %= 500

if num >= 100: 
    print("แลกเงิน แบงค์ 100 => ", num//100 ,"  ใบ")
    num %= 100

if num >= 50 : 
    print("แลกเงิน แบงค์ 50 => ", num//50 , "  ใบ")
    num %= 50

if num >= 20 :
    print("แลกเงิน แบงค์ 20 => ", num//20 , "  ใบ")
    num %= 20

  