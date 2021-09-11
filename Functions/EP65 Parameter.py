
def add(x,y,z) :
    print(x+y+z)

def odd(*args) :
    sum=0
    for i in args:
        sum+=i
    print(sum)


#main
add(10,10,0)
add(5,6,10)
odd(1,2,3,4,5,6,7,8,9)