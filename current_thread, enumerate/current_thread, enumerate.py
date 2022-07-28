"""
    current_thread:
        Return the current Thread object, corresponding to the caller’s thread of control.
        If the caller’s thread of control was not created through the threading module,
            a dummy thread object with limited functionality is returned.


    enumerate:
        Return a list of all Thread objects currently active.
        The list includes daemonic threads and dummy thread objects created by current_thread().
        It excludes terminated threads and threads that have not yet been started. However,
            the main thread is always part of the result, even when terminated

    active_count:
        Return the number of Thread objects currently alive.
        The returned count is equal to the length of the list returned by enumerate().
"""

from time import sleep
from threading import Thread, current_thread, enumerate, active_count


def show(name):
    print(f'starting {name}...')
    print(current_thread())
    print(current_thread().name)  # first: Thread One , second: Thread Two
    print(enumerate())  # [<_MainThread(MainThread, started 139990680201024)>, <Thread(Thread One, started 139990672950848)>, <Thread(Thread Two, started 139990664558144)>]
    print(active_count())  # 3
    sleep(3)
    print(f'finishing {name}.')


thread_one = Thread(target=show, args=('One',), name='Thread One')
thread_two = Thread(target=show, args=('Tow',), name='Thread Two')

thread_one.start()
thread_two.start()

thread_one.join()
thread_two.join()

print('Done')
