import threading
import time
def square(n):
    for i in n:
        time.sleep(1)
        print("Square=",i*i)

def cube(n):
    for i in n:
        time.sleep(1)
        print("Cube=",i*i*i)

a=[2,3,8,9]
t1=time.time()

ob1=threading.Thread(target=square,args=(a,))
ob2=threading.Thread(target=cube,args=(a,))
ob1.start()
ob2.start()
ob1.join()
ob2.join()

t2=time.time()
print("Execution Time=",t2-t1)
