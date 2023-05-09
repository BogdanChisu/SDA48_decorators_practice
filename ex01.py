"""
creati un decorator pentru a masura performanta unei functii.
Ca exemplu puteti testa cu functia recurenta de fibonacci (pentru ca ia relativ mult timp) sau alte functii. (edited)
"""

from time import perf_counter

time_start = perf_counter()

def perf_decorator(func):

    def wrapper(*args):
        print(f"Took = {perf_counter() - time_start}s")
        return func(*args)
    return wrapper

@perf_decorator
def fibonacci_recurent(n):
    if not isinstance(n, int) or n <= 0:
        return None
    if n in (1, 2):
        return 1
    return fibonacci_recurent(n - 1) + fibonacci_recurent(n - 2)

nth = 30
nth_element = fibonacci_recurent(nth)
print(f"The {nth}th element of recursive Fibonacci equals = {nth_element}")
print(f"Took = {perf_counter() - time_start}")