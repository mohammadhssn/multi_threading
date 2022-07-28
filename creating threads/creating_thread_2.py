from time import sleep, perf_counter
from threading import Thread

start = perf_counter()


def show(name, delay):
    print(f'starting {name}...')
    sleep(delay)
    print(f'finishing {name}.')


class ShowThread(Thread):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay

    def run(self):
        show(self.name, self.delay)


thread_one = ShowThread('One', 4)
thread_two = ShowThread('Two', 8)

thread_one.start()
thread_two.start()

thread_one.join()
thread_two.join()

end = perf_counter()

print(round(end - start))
