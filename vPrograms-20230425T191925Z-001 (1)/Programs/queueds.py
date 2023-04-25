from queue1 import queue
q=queue()
choice=0
while choice<4:
    print("1-ENQUEUE")
    print("2-DEQUEUE")
    print("3-SEARCH")
    print("4-EXIT")
    choice=int(input("Enter Choice="))
    if choice==1:
        element=int(input("Enter element="))
        q.enqueue(element)
        print("Queue=",q.display())
    elif choice==2:
        element=q.dequeue()
        if element==-1:
            print("Queue is empty..")
        else:
            print("Deleted Element=",element);
            print("Queue=",q.display())
    elif choice==3:
        element=int(input("Enter element to be searched="))
        p=q.search(element)
        if p==-1:
            print("Queue is empty..")
        elif p==-2:
            print("Element is not present")
        else:
            print("Element is present at position=",p)
    else:
        break
        
