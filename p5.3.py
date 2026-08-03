import threading

print("Shreyash Kadam S091")

lock = threading.Lock()

def print_even():
    with lock:
        print("Even Numbers:")
        for i in range(1, 11):
            if i % 2 == 0:
                print(i, end=" ")
        print()

def print_odd():
    with lock:
        print("Odd Numbers:")
        for i in range(1, 11):
            if i % 2 != 0:
                print(i, end=" ")
        print()

def reverse_string(text):
    with lock:
        print("\nOriginal String:", text)
        print("Reversed String:", text[::-1])

t1 = threading.Thread(target=print_even)
t2 = threading.Thread(target=print_odd)
t3 = threading.Thread(target=reverse_string, args=("Data Science",))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("\nAll threads completed.")
