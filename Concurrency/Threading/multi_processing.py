from concurrent.futures import ProcessPoolExecutor


def square_number(num):
    return f"Square:{num*num}"


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=8) as executor:
        results = executor.map(square_number, numbers)

    for res in results:
        print(res)
