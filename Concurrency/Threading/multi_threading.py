from concurrent.futures import ThreadPoolExecutor
import time


def print_number(num):
    print(f"Number:{num}")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

with ThreadPoolExecutor(max_workers=len(numbers)) as executor:
    results = executor.map(print_number, numbers)

print(results)
