"""
    Event:
        Event objects are used when you want to communicate with several threads and be aware of each other's status.
        In these objects, by using the set method, the nodes can declare their readiness to do the work,
        and with the wait method, they can declare that they are waiting for a response from the other nodes.
        In this case, other threads can work together again with the set method connected to the previous thread
"""

from threading import Thread, Event
from time import sleep


def first(f, s):
    sleep(30)
    print('first is ready ...')
    f.set()
    s.wait()
    print('first is working ...')
    f.clear()


def second(f, s):
    print('second is ready ...')
    s.set()
    f.wait()
    print('second is working ...')
    s.clear()


first_event = Event()
second_event = Event()

first_thread = Thread(target=first, args=(first_event, second_event))
second_thread = Thread(target=second, args=(first_event, second_event))

first_thread.start()
second_thread.start()
