# sum
def summation(num):
    total,avg=0,0
    for i in num:
        total+=i
    avg=total/len(num)
    return total,avg



x=[1,2,3,4,5,6,7,8]
y,z=summation(x)

print(y)
print(z)
