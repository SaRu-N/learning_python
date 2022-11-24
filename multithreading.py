import threading
import time
def print_hello():
    for i in range(3):
        time.sleep(0.8)
        print("Hello")
def print_hi():
    for i in range(3):
        time.sleep(0.4)
        print("Hi")

t1=threading.Thread(target=print_hello)
t2=threading.Thread(target=print_hi)

t1.start()
t2.start()