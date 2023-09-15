from concurrent.futures import ThreadPoolExecutor
from time import sleep


def show(name):
    print(f"Starting {name} ...")
    sleep(3)
    print(f"Finigshing {name} ...")


with ThreadPoolExecutor(max_workers=2) as executor:
    names = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']
    executor.map(show, names)

print("done...")