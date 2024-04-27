n=int(input("enter number of element:"))
a=[]
for i in range(n):
    a.append(int(input("enter element:")))
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if(a[i]>a[j]):
            flag=0
        else:
            flag=1
            break
    if(flag==0):
        if(a[i]==1):
            break
        else:
            print(a[i])
print(a[-1])   
    
            
    
    
