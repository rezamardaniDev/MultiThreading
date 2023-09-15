from threading import Thread, current_thread, enumerate
from time import sleep


def show(name):
    print(f"Starting {name} ...")
    print(current_thread())  # return the current thread object
    print(enumerate())  # return alive threads
    print()
    sleep(3)
    print(f"Finigshing {name} ...")


t1 = Thread(target=show, args=('one',), name="t1")
t2 = Thread(target=show, args=('two',), name="t2")

t1.start()
t2.start()

t1.join()
t2.join()

print("done...")