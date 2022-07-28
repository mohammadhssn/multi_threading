"""
    Timer:
        Using this class, you can execute your functions after a certain period of time.
        The thing you should pay attention to is that this time is not exact and may be less or more.
"""

from threading import Timer


def show():
    print('show is start')


timers = Timer(5, show)
timers.start()
