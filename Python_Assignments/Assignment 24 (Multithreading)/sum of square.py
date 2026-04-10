"""1. Calculate the sum of squares of numbers from 1 to 100 using four threads. Divide the
range equally among the threads, and each thread calculates the sum of squares for its
range. Finally, combine the results to get the total sum of squares."""
import threading

total_sum = 0
lock = threading.Lock()

def sum_of_squares(start, end):
    global total_sum
    local_sum = sum(i*i for i in range(start, end+1))
    with lock:
        total_sum += local_sum

# Divide 1-100 into 4 ranges
ranges = [(1,25), (26,50), (51,75), (76,100)]
threads = []

for start, end in ranges:
    t = threading.Thread(target=sum_of_squares, args=(start,end))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Total sum of squares from 1 to 100 is:", total_sum)
