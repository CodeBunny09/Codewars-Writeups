"""
It said "Implement the memorization solution!"
I was new to it, so I came up with:
YouTube:-
Programming Terms: Memoization:  https://www.youtube.com/watch?v=a7EjmdQzPqY
Recursion and Memoization Tutorial Python: https://www.youtube.com/watch?v=sCecRPSQg6Y
"""
#given code
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

#Final Solution
cache = {}
def fibonacci(n):
    if n in [0, 1]:
        return n
    if n in cache:
        return cache[n]
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
        cache[n] = result
        return result