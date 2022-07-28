"""
    ThreadPoolExecuter:
        In normal mode, the Thread class is used to create a thread.
        But the problem with the Thread class is that if you need to create a large number of threads,
            you have to write more code. But by using the ThreadPoolExecuter class,
            you can easily create a large number of threads with the least possible code.
"""

from concurrent.futures import ThreadPoolExecutor
from time import sleep


def show(name):
    print(f'starting {name}...')
    sleep(3)
    print(f'finishing {name}.')


with ThreadPoolExecutor(max_workers=2) as executer:
    names = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven']

    executer.map(show, names)

print('Done')
