# Factorial
"""
5! = 5 * 4 * 3 * 2 * 1
"""

def Factorial(num) :
    if num == 1 :
        return num
    else :
        return num * Factorial(num-1)
    


x=Factorial(8)
print("ค่า ! : ",x)