import time
import threading

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Number: {i}")

def print_letters():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")

# create two threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)


t = time.time() 

# start thread
t1.start()
t2.start()

# Wait for threads to complete
t1.join()
t2.join()


finish_time = time.time() - t   # elapsed time
print(f"Execution time: {finish_time:.4f} seconds")
