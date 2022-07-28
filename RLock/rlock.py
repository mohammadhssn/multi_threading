"""
    RLock:
       you will learn about the Rlock class in Python threading. In the previous meetings,
        you saw that by using lock,we could make the threads respect each other's work and wait for the shared resource
          until the work of one thread is finished. And you saw that if we acquire several times using one thread,
          our code gets blocked and the program crashes, and to solve this problem, we used lock as a context manager.
          But when our program needs to call a method several times or the program is recursive,
          using lock as a context manager will not be useful and the program will be blocked. In this case,
          you can use Rlock instead of lock.
          By using Rlock, you can acquire several times without the program being blocked.
"""

from threading import RLock, Thread

num = 0
rlock = RLock()


def add():
    global num
    with rlock:
        subtract()
        for _ in range(100000):
            num += 1


def subtract():
    global num
    with rlock:
        for _ in range(100000):
            num -= 1


def both():
    add()
    subtract()


thread_both = Thread(target=both)

thread_both.start()

thread_both.join()

print(f'num: {num}')
print('Done')
