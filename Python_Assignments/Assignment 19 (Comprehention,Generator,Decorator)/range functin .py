'''3. Write a generator function that mimics the behavior of the built-in
range() function. The generator should take start, stop, and step
arguments and yield numbers within the specified range.'''

def custom_range(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0
    
    if step == 0:
        raise ValueError("step cannot be zero")
    
    if step > 0:
        while start < stop:
            yield start
            start += step
    else:
        while start > stop:
            yield start
            start += step 

print("Range like built-in:")
for num in custom_range(2, 10, 2):
    print(num, end=" ")
