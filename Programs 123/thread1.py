import threading
import time
class A(threading.Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            time.sleep(0.5)

class B(threading.Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            time.sleep(0.5)

a=A()
b=B()
a.start()
b.start()
a.join()
b.join()
print("END...")
