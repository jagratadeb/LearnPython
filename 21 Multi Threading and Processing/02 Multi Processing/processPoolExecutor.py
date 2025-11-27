from concurrent.futures import ProcessPoolExecutor
import time

def print_number(number):
    # Simulate a heavy computation
    time.sleep(2)
    return f"Number: {number}"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use ProcessPoolExecutor instead of ThreadPoolExecutor
if __name__ == "__main__":
    start = time.time()

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(print_number, numbers)

    for result in results:
        print(result)

    finish = time.time() - start
    print(f"Execution time: {finish:.4f} seconds")
