n=int(input("enter the amount:"))
m=int(input("enter the curreny notes of denomination for withdrawn:"))
if(m==10):
    print("total number of currency notes of Rs 10 denomination:",n//10)
elif(m==100):
    print("total number of currency notes of Rs 100 denomination:",n//100)
elif(m==50):
    print("total number of currency notes of Rs 50 denomination:",n//50)
else:
    print("invalid input")

