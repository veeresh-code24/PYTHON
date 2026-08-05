# Without MultiThreading

'''import time

def task(name):
    print(f"{name} started")
    time.sleep(3)

    print(f"{name} finished")


task("Task 1")
task("Task 2")
task("Task 3")'''


# with Multhithreading

import threading
import time

def task(name):
    print(f"{name} started")
    time.sleep(3)
    print(f"{name} finished")

t1 = threading.Thread(target=task, args=("Task 1",))
t2 = threading.Thread(target=task, args =("Task 2", ))

t1.start()
t2.start()

t1.join()
t2.join()

print("All Task Completed")