from multiprocessing import Process, Semaphore, Lock, Array, Value
import time
import random


BUFFER_SIZE = 5
ITEM_COUNT = 10


def producer(shared_buffer, write_pos, read_pos, empty_slots, filled_slots, buffer_lock):
    for _ in range(ITEM_COUNT):
        value = random.randint(1, 100)

        empty_slots.acquire()
        buffer_lock.acquire()

        position = write_pos.value
        shared_buffer[position] = value
        print(f"[Producer] Produced item {value} at index {position}", flush=True)

        write_pos.value = (position + 1) % BUFFER_SIZE

        buffer_lock.release()
        filled_slots.release()

        time.sleep(random.uniform(0.1, 0.3))


def consumer(shared_buffer, write_pos, read_pos, empty_slots, filled_slots, buffer_lock):
    print("[Consumer] Process started", flush=True)

    for _ in range(ITEM_COUNT):
        filled_slots.acquire()
        buffer_lock.acquire()

        position = read_pos.value
        value = shared_buffer[position]
        print(f"[Consumer] Consumed item {value} from index {position}", flush=True)

        read_pos.value = (position + 1) % BUFFER_SIZE

        buffer_lock.release()
        empty_slots.release()

        time.sleep(random.uniform(0.1, 0.3))


def main():
    shared_buffer = Array('i', BUFFER_SIZE)
    write_pos = Value('i', 0)
    read_pos = Value('i', 0)

    empty_slots = Semaphore(BUFFER_SIZE)
    filled_slots = Semaphore(0)
    buffer_lock = Lock()

    print("Shreyash Kadam S091")

    print("Starting processes...", flush=True)

    producer_process = Process(
        target=producer,
        args=(shared_buffer, write_pos, read_pos, empty_slots, filled_slots, buffer_lock)
    )

    consumer_process = Process(
        target=consumer,
        args=(shared_buffer, write_pos, read_pos, empty_slots, filled_slots, buffer_lock)
    )

    producer_process.start()
    consumer_process.start()

    producer_process.join()
    consumer_process.join()

    print("Producer and Consumer processes have finished.", flush=True)


if __name__ == "__main__":
    main()
