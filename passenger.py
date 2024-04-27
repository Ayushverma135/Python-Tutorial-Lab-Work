airline=input("enter the airline:")
source=input("enter source:")
destination=input("enter destination:")
passengers=int(input("enter number of passengers:"))
a=[]
for i in range(passengers):
        a.append(airline+":"+source[0:3]+":"+destination[0:3]+":"+str(101+i))
if(passengers<5):
    for i in range(passengers):
        print(a[i])
else:
    for i in range(passengers-5,passengers):
        print(a[i])
