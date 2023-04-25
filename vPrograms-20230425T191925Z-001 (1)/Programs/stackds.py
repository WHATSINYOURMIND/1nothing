from stack import stack
s=stack()
choice=0
while choice<5:
    print("1-PUSH")
    print("2-POP")
    print("3-PEEK")
    print("4-SEARCH")
    print("5-EXIT")
    choice=int(input("Enter Choice="))
    if choice==1:
        element=int(input("Enter element="))
        s.push(element)
        print("Stack=",s.display())
    elif choice==2:
        element=s.pop()
        if element==-1:
            print("Stack is empty..")
        else:
            print("Popped Element=",element);
            print("Stack=",s.display())
    elif choice==3:
        element=s.peek()
        print("Top Element=",element)
    elif choice==4:
        element=int(input("Enter element to be searched="))
        p=s.search(element)
        if p==-1:
            print("Stack is empty..")
        elif p==-2:
            print("Element is not present")
        else:
            print("Element is present at position=",p)
    else:
        break
        
