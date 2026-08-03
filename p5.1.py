import threading

print("Shreyash Kadam S091")


results = []


lock = threading.Lock()

def generate_fibonacci(n):
    a, b = 0, 1
    sequence = []

    for i in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence


def task(n):
    sequence = generate_fibonacci(n)

    
    with lock:
        results.append((n, sequence))
        print(f"Thread: {threading.current_thread().name}")
        print(f"Fibonacci({n}) = {sequence}\n")


values = [4, 5, 6]

threads = []


for n in values:
    t = threading.Thread(target=task, args=(n,))
    threads.append(t)
    t.start()
.
for t in threads:
    t.join()

print("Shared Results:")
print(results)

print("\nAll threads completed.")
