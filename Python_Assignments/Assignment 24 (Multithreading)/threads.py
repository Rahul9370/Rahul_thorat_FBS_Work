"""4. Implement a producer-consumer problem with a limited buffer of size 5. Create two
producer threads and two consumer threads. Producers produce items, and consumers
consume them. Ensure proper synchronization to avoid buffer overflows or underflows."""
import threading
import time
import random
from queue import Queue

buffer_size = 5
buffer = Queue(buffer_size)

def producer(name):
    for i in range(10):
        item = random.randint(1, 100)
        buffer.put(item)  # automatically waits if buffer is full
        print(f"{name} produced: {item}")
        time.sleep(random.uniform(0.1, 0.5))

def consumer(name):
    for i in range(10):
        item = buffer.get()  # automatically waits if buffer is empty
        print(f"{name} consumed: {item}")
        buffer.task_done()
        time.sleep(random.uniform(0.2, 0.6))

p1 = threading.Thread(target=producer, args=("Producer-1",))
p2 = threading.Thread(target=producer, args=("Producer-2",))
c1 = threading.Thread(target=consumer, args=("Consumer-1",))
c2 = threading.Thread(target=consumer, args=("Consumer-2",))

p1.start()
p2.start()
c1.start()
c2.start()

p1.join()
p2.join()
buffer.join()  # wait until all items consumed
c1.join()
c2.join()
