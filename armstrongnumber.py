n=int(input())
count=len(str(n))
Sum=0
temp=n
print(count)
while(temp!=0):
    a=temp%10
    Sum+=a**count
    temp=temp//10
if(n==Sum):
    print("armstrong number")
else:
    print("not an armstrong number")
