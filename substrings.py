str1=input("enter string:")
a=[]
for i in range(len(str1)):
    for j in range(i+1,len(str1)):
        a.append(str1[i:j+1])
print(set(a))
