from threading import Timer


def show():
    print("Hello!")


t = Timer(10, show)
t.start()
