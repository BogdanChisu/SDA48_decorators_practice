"""
Scrieti un decorator pentru a verifica daca un numar este par sau impar.
"""
def deco_is_odd(func):

    def wrapper(*args):
        func(*args)
        for arg in args:
            if args[0] % 2 == 1:
                print(f"{args[0]} is odd")
            else:
                print(f"{args[0]} is even")
    return wrapper
@deco_is_odd
def functia_mea(v1):
    print(f"Numarul este {v1}")

functia_mea(16)