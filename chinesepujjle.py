no_heads=int(input("enter no. of heads:"))
no_legs=int(input("enter no. of legs:"))
if(no_legs%2!=0):
    print("no solution")
elif(no_heads*4==no_legs):
    print("rabbits",no_heads,"chickens",0)
elif(no_heads%2==no_legs):
    print("rabbits",0,"chickens",no_heads)
else:
    
