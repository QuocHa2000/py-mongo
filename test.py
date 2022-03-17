import time
import threading


def func1():
    print("Start 1")
    time.sleep(5)
    print("End 1")


def func2():
    print("Start 2")
    time.sleep(5)
    print("End 2")


t = time.time()

thread1 = threading.Thread(target=func1, args=())
thread2 = threading.Thread(target=func2, args=())

thread1.start()
thread2.start()

thread1.join()
thread2.join()

# func1()
# func2()

print("End", time.time()-t)
