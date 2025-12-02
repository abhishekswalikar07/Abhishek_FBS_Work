# Implement two threads to print lowercase and uppercase alphabets concurrently from
# 'a' to 'z' and 'A' to 'Z'.

from threading import Thread, Lock
import time

lower_lock = Lock()
upper_lock = Lock()

def lowercase(start,end):
    for i in range(start,(end+1)):
            lower_lock.acquire()
            print(chr(i),end=" ")
            upper_lock.release()
            time.sleep(0.01)

def uppercase(start,end):
    for i in range((start),(end+1)):
            upper_lock.acquire()
            print(chr(i),end=" ")
            lower_lock.release()
            time.sleep(0.01)

if __name__=='__main__':
    lock=Lock()
    upper_lock.acquire()
    # lock.acquire()
    t1=Thread(name='Thread1',target=lowercase,args=(65,90))
    t2=Thread(name='Thread2',target=uppercase,args=(97,122))

    t1.start()
    t2.start()
    # lock.release()
    t1.join()
    t2.join()