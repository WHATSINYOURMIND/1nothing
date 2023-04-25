def max(x,y):
    if x>y:
        return x
    else:
        return y

a,b,c,d=map(int,input("Enter 4 numbers=").split())
e=max(a,b)
e=max(e,c)
e=max(e,d)
print("Largest Number=",e)
        
