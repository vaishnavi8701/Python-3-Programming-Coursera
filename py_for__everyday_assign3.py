#assignemt3.1
hrs =float(input("Enter Hours:"))
rate=float(input("enter rate: "))
if(hrs>40):
    hrs=hrs-40
    pay=(40*rate)+(hrs*rate*1.5)
    print(pay)
else:
    pay(40*rate)
    print(pay)
    
#assigment 3.3

score = float(input("Enter Score: "))
if(score>=0.9 and score<=1.0):
    print("A")
elif(score>=0.8 and score<0.9):
    print("B")
elif(score>=0.7 and score<0.8):
    print("C")
elif(score>=0.6 and score<0.7):
    print("D")
elif(score<0.6):
    print("F")
else:
    print("error")
