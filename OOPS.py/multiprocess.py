from multiprocessing import Process
import time

def square(n):
    print(f" Calculating {n} ")
    time.sleep(2)
    print(n*n)

if __name__ == "__main__":



    p1 = Process(target = square, args =(5,))
    p2 = Process(target = square, args =(10,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Finished")
