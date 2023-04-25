import array
a=array.array('i',[])
n=int(input("Enter number of elements="))
for i in range(0,n):
    x=int(input("Enter Number="))
    a.append(x)
sum=0
for i in a:
    sum=sum+i
print("Sum of array elements=",sum)
    
