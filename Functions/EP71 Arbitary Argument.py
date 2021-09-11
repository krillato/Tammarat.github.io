#แบบ ระบุ key โดยใช้ kwargs

def add(*number):  # *args => ค่าใน parameter มีได้หลายค่า
    sum=0
    for i in range(len(number)):
        sum+=number[i]
    print(sum)

add(10,5)
add(5+9+8)

def displatdata(**kwargs) :  # **kwargs คำสั่งในการดึง keyword มาใช้
    print(kwargs)
    print(kwargs["status"])


displatdata(fname="ธรรมรัต",lname="ชาญสมร",city="นนทบุรี",status="โสด")
displatdata(fname="ธรรมรัต",lname="ชาญสมร",status="โสด")
displatdata(sing="ธรรมรัต",lname="ชาญสมร",status="โสด")