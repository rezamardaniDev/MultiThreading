from threading import Thread, RLock

"""
    Race Condition
    Thread Safe
    Dead Lock
    atomic
"""

lock = RLock()
num = 0  # shared resource


def add():
    global num
    with lock:
        subtract()
        for _ in range(100000):
            num += 1


def subtract():
    global num
    lock.acquire()
    for _ in range(100000):
        num -= 1
    lock.release()


def both():
    subtract()
    add()


t1 = Thread(target=both)

t1.start()

t1.join()

print(num)
print("done...")
