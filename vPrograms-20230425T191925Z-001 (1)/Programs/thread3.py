import threading
x=0
def f1(l):
    l.acquire()
    global x
    for i in range(100000):
        x=x+1
    l.release()

def f2():
    l=threading.Lock()
    t1=threading.Thread(target=f1,args=(l,))
    t2=threading.Thread(target=f1,args=(l,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

f2()
print(x)
    
    
