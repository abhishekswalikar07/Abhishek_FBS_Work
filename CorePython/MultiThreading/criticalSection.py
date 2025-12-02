from threading import Thread, Lock
import time

def withdraw(amt):
    lock.acquire()
    with open('CorePython/MultiThreading/amount.txt','r') as fp:
        conetnt=fp.read()
        bal=int(conetnt)
        bal-=amt
    with open('CorePython/MultiThreading/amount.txt','w') as fp:
        fp.write(str(bal))
    lock.release()

def deposite(amt):
    lock.acquire()
    with open('CorePython/MultiThreading/amount.txt','r') as fp:
        conetnt=fp.read()
        bal=int(conetnt)
        bal+=amt
    with open('CorePython/MultiThreading/amount.txt','w') as fp:
        fp.write(str(bal))
    lock.release()

if __name__=='__main__':
    lock=Lock()
    t1=Thread(name='Thread1',target=deposite,args=(5000,))
    t2=Thread(name='Thread2',target=withdraw,args=(3000,))
    t1.start()
    t2.start()