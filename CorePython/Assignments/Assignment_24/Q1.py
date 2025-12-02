# Calculate the sum of squares of numbers from 1 to 100 using four threads. Divide the
# range equally among the threads, and each thread calculates the sum of squares for its
# range. Finally, combine the results to get the total sum of squares.

from threading import Thread,Lock
import time

sum_list=[]
def square(start,end):
    sum=0
    for i in range(start,end+1):
        sum+=i**2
    # print(sum)
    sum_list.append(sum)
    # print(sum_list)

    

if __name__=='__main__':
    lock=Lock()
    t1=Thread(name='Thread1',target=square,args=(1,25))
    t2=Thread(name='Thread2',target=square,args=(26,50))
    t3=Thread(name='Thread3',target=square,args=(51,75))
    t4=Thread(name='Thread4',target=square,args=(76,100))
    
    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    addition=0
    print("Addition of all squares from numbers 1 to 100 is:")
    for i in sum_list:
        addition+=i
    print(addition)