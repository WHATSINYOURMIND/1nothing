l1=[]
l1.append("CP")
l1.append("JAVA")
l1.append("Python")
print("The Existing List=",l1)
choice=0
while choice<5:
    print("1-Insert Element")
    print("2-Remove Element")
    print("3-Replace Element")
    print("4-Search Element")
    print("5-Exit")
    choice=int(input("Enter Choice="))
    if choice==1:
        element=input("Enter element to be inserted=")
        pos=int(input("Enter position of element="))
        l1.insert(pos,element)
        print("List=",l1)
    elif choice==2:
        try:
            element=input("Enter element to be removed=")
            l1.remove(element)
        except ValueError:
            print("Element not found...")
        else:
            print("List=",l1)
    elif choice==3:
        element=input("Enter element which will replace existing element=")
        pos=int(input("Enter position of element to be replaced="))
        l1.pop(pos)
        l1.insert(pos,element)
        print("List=",l1)
    elif choice==4:
        element=input("Enter element to be searched=")
        try:
            p=l1.index(element)
            print("Element is present at position=",p)
        except ValueError:
            print("Element is not present...")
        else:
            print("List=",l1)
    else:
        break
            
        

    
