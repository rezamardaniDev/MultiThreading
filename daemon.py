import sys
from threading import Thread
from time import sleep


def show(name):
    print(f"Starting {name} ...")
    sleep(3)
    print(f"Finigshing {name} ...")


t1 = Thread(target=show, args=('one',), daemon=False)
t2 = Thread(target=show, args=('two',), daemon=False)

# t1.setDaemon(True)

t1.start()
t2.start()

# t1.isDaemon()

print("done...")
sys.exit()
