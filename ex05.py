"""
Scrieti un decorator care printeaza "String invalid" daca unul din argumentele functiei
este string ce conține unul sau mai multe caractere speciale (hint: cu reg-ex)
"""
import re

def deco_func_has_special(func):

    def wrapper(*args):
        func(*args)
        for arg in args:
            results = re.findall(r"\W", arg)
            if results:
                print(f"String invalid:\n{arg}")
            else:
                print(f"String valid:\n{arg}.")

    return wrapper

@deco_func_has_special
def my_function(*args):
    print(f"Parameters are '{args}'")

my_function("2343", "445!46", "#$$%98734jh")