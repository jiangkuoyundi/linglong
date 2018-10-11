#-*- coding: utf-8 -*-
import threading
import time
from time import sleep, ctime
def thread1():
    print(1)

def thread2():
    print(2)
    time.sleep(2)
    print(2)
    time.sleep(2)

if __name__ == '__main__':
    threads = []

    t1 = threading.Thread(target=thread1())

    t2 = threading.Thread(target=thread2())

    threads.append(t1)

    threads.append(t2)

    for t in threads:
        t.start()

    print(ctime())