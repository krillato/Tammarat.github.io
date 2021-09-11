x = 10
y = 3.14 
z = "25"

#บวกเลข 
ans=x+y

print(type(x))
print(type(y))
print(type(z))
print(ans)

# การแปลงชนิดข้อมูล   string => int
bns = x + int(z)
print(bns)

# การแปลงชนิดข้อมูล    int  => string 
cns = str(x) + z
print(cns)
print(type(cns))

# การแปลงชนิดข้อมูล    string => float
z=float(z)
print(z)

