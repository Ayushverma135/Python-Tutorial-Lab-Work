n=int(input("enter number"))
a=[]
for i in range(n):
    a.append(int(input("enter element:")))
mut=1
for i in range(n):
    if(a[i]==7):
        for j in range(i+1,n):
            mut=mut*a[j]
print(mut)
