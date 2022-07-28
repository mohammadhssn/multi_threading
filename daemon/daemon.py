"""
    In the computer world, a daemon is a program that can work in the background. But in Python,
     a daemon is a thread that the program can ignore and exit. By default, the value of daemon is False,
      which means that the program has to wait until the thread finishes.
"""
import sys
from time import sleep, perf_counter
from threading import Thread

start = perf_counter()


def show(name):
    print(f'starting {name}...')
    sleep(3)
    print(f'finishing {name}.')


thread_one = Thread(target=show, args=('One',), daemon=True)
thread_two = Thread(target=show, args=('Tow',), daemon=True)

thread_one.start()
thread_two.start()

# thread_one.join()  # If join() is used. The daemon is ignored
# thread_two.join()  # If join() is used. The daemon is ignored

print(thread_one.daemon)  # True
print(thread_two.daemon)  # True

end = perf_counter()
sys.exit()
