"""
1. Develop a memoization decorator that caches the results of function
calls and returns the cached result when the same inputs occur again.
This can greatly improve the performance of recursive or
computationally intensive functions."""

def memoize(func):
    cache = {}
    
    def wrapper(*args):
        if args in cache:
            print(f"Fetching from cache for {args}")
            return cache[args]
        print(f"Computing result for {args}")
        result = func(*args)
        cache[args] = result
        return result
    
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
print(fibonacci(9))  
