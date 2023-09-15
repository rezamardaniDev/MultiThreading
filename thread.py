from time import sleep, perf_counter
from threading import Thread

start = perf_counter()


def show(name):
    print(f"Starting {name} ...")
    sleep(3)
    print(f"Finigshing {name} ...")


t1 = Thread(target=show, args=('one',))
t2 = Thread(target=show, args=('two',))

t1.start()
t2.start()

t1.join()
t2.join()

end = perf_counter()
print(round(end - start))
