def Tower_of_hanoi(n,source,destination,auxilary):
    if(n==1):
        print("move disk 1 from source",source,"to destination",destination)
        return
    Tower_of_hanoi(n-1,source,auxilary,destination)
    print("move disk",n,"from source",source,"to destination",destination)
    Tower_of_hanoi(n-1,auxilary,destination,source)
n=4
Tower_of_hanoi(n,'a','b','c')
