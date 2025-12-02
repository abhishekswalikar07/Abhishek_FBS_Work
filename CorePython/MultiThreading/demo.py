from threading import Thread
import time
def fun1(str1):
    for i in str1:
        print(i,end=' ',flush=True)
        time.sleep(1)
def fun2(str2):
    for i in str2:
        print(i,end=' ',flush=True)
        time.sleep(1)
    
if __name__=='__main__':
    t1=Thread(name='Thread1',target=fun1, args=('11111',))
    t2=Thread(name='Thread2',target=fun2,args=('22222',))
    t1.start()
    t1.join(4)
    t2.start()
    print('This is executed by main thread')