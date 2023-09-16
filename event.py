from threading import Event, Thread
from time import sleep


def first(f, s):
    sleep(30)
    print("first is ready!")
    f.set()
    s.wait()
    print("first is working")
    f.clear()


def second(f, s):
    print("second is ready!")
    s.set()
    f.wait()
    print("second is working")
    s.clear()


f = Event()
s = Event()

t1 = Thread(target=first, args=(f, s))
t2 = Thread(target=second, args=(f, s))

t1.start()
t2.start()