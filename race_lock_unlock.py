from threading import Thread, Lock

"""
    Race Condition
    Thread Safe
    Dead Lock
"""

lock = Lock()
num = 0  # shared resource


def add():
    global num
    with lock:
        for _ in range(100000):
            num += 1


def subtract():
    global num
    lock.acquire()
    for _ in range(100000):
        num -= 1
    lock.release()


t1 = Thread(target=add)
t2 = Thread(target=subtract)

t1.start()
t2.start()

t1.join()
t2.join()

print(num)
print("done...")
