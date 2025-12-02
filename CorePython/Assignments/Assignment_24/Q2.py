# Create two threads, one printing even numbers and the other printing odd numbers
# from 1 to 10. Ensure proper synchronization to alternate between even and odd numbers.

from threading import Thread, Lock
import time

odd_lock = Lock()
even_lock = Lock()

def odd(start,end):
    for i in range(start,end+1):
        
        if i%2!=0:
            odd_lock.acquire()
            print(i,end=" ")
            even_lock.release()
            time.sleep(0.01)

def even(start,end):
    for i in range(start,end+1):
        
        if i%2==0:
            even_lock.acquire()
            print(i,end=" ")
            odd_lock.release()
            time.sleep(0.01)

if __name__=='__main__':
    lock=Lock()
    even_lock.acquire()
    # lock.acquire()
    t1=Thread(name='Thread1',target=odd,args=(1,10))
    t2=Thread(name='Thread2',target=even,args=(1,10))

    t1.start()
    t2.start()
    # lock.release()
    t1.join()
    t2.join()