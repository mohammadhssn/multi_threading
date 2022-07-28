from time import sleep, perf_counter
from threading import Thread

start = perf_counter()


def show(name):
    print(f'starting {name}...')
    sleep(3)
    print(f'finishing {name}.')


thread_one = Thread(target=show, args=('One',))
thread_two = Thread(target=show, args=('Tow',))

thread_one.start()
thread_two.start()

thread_one.join()
thread_two.join()

end = perf_counter()
print(round(end - start))
