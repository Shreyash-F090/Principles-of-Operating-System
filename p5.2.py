import threading

print("Shreyash Kadam S091")


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


def task(n):
    result = factorial(n)
    print(f"\nFactorial of {n} = {result}")


if __name__ == "__main__":

    print("Multi-threaded Factorial Calculator\n")

    
    numbers = [4, 5, 6]

    threads = []

    
    for n in numbers:
        t = threading.Thread(target=task, args=(n,))
        threads.append(t)
        t.start()

    
    for t in threads:
        t.join()

    print("\nAll threads completed.")
