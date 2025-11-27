import time
import multiprocessing

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i*i*i}")

if __name__ == "__main__":
    # create two process
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    # start timer
    t = time.time() 

    # start process
    p1.start()
    p2.start()

    # Wait for threads to complete
    p1.join()
    p2.join()


    finish_time = time.time() - t   # elapsed time
    print(f"Execution time: {finish_time:.4f} seconds")
