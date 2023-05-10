"""
Scrieti un decorator pentru a verifica daca un numar este par sau impar.
"""
def deco_is_odd(func):

    def wrapper(*args):
        func(*args)
        for arg in args:
            if arg % 2 == 1:
                print(f"{arg} is odd")
            else:
                print(f"{arg} is even")
    return wrapper
@deco_is_odd
def functia_mea(*args):
    print(f"Numarele sunt {args}")

functia_mea(16, 17, 19)