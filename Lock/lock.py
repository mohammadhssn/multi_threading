"""
    Lock : https://docs.python.org/3/library/threading.html#lock-objects

    Race condition:
        Race condition problem occurs when two or more threads want to access a shared resource at the same time.
        In this case, the second thread may access the shared resource while the first thread is working
         and receive the incomplete information that the first thread was working on.

    Thread safe:
        To solve this race condition problem, the Lock class should be used to lock the program using the acquire method
         so that another thread cannot access the resources and
         release the program after finishing the work with the release method.
         In this case, the program will be thread safe

    Dead lock:
        The dead lock problem occurs when we mistakenly lock the program that was locked using the acquire method again
         with the acquire method. In this case,
         the program is blocked and neither a response is returned nor the program ends. To solve this problem,
         it is suggested to use lock as a context manager with the with method.
"""

from threading import Thread, Lock

num = 0
lock = Lock()


def add():
    global num
    with lock:
        for _ in range(100000):
            num += 1


def subtract():
    global num
    with lock:
        for _ in range(100000):
            num -= 1


thread_add = Thread(target=add)
thread_subtract = Thread(target=subtract)

thread_add.start()
thread_subtract.start()

thread_add.join()
thread_subtract.join()

print(f'num: {num}')
print('Done')
