"""
    Semaphore:
        In this video, you will learn about semaphore in Python threading.
        semaphore has a function similar to lock,
         but it is used for times when you need to control the number of threads that connect to a shared resource.
        In the semaphore class, there is a counter that controls the number of connected threads.
        Every time a thread uses the acquire method, a number is subtracted from this counter,
         and every time the release method is used, it is added to this number. When this number reaches zero,
          no other threads are accepted and they have to wait. In this video,
          you will also learn about the BoundedSemaphore class. In the semaphore class,
           if you use release more than the number of acquires,
           the number of counters becomes negative and causes more threads to work in the next step.
        To solve this problem, you can use the BoundedSemaphor class,
         which will give a ValueError error message if the counter becomes negative.
"""

from threading import Thread, Semaphore, BoundedSemaphore, current_thread
from time import sleep

lock = Semaphore(value=2)
# lock = BoundedSemaphore(value=2) #BoundedSemaphore

num = 0


def add():
    global num
    with lock:
        print(current_thread().name)
        sleep(2)
        num += 1


t1 = Thread(target=add)
t2 = Thread(target=add)
t3 = Thread(target=add)
t4 = Thread(target=add)
t5 = Thread(target=add)
t6 = Thread(target=add)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()

print(f'num: {num}')
print('Done')
