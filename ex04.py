"""
Scrieti un decorator care printeaza daca o variabila a functiei contine cel putin o vocala.
"""
import re

def deco_func_has_vowel(func):

    def wrapper(*args):
        func(*args)
        for arg in args:
            if re.search(r"[aeiouAEIOU]", arg):
                print(f"There is at least one vowel in one func parameter.\n{arg}")
                break
        else:
             print(f"No vowels in this DJERMAN strings.")

    return wrapper

@deco_func_has_vowel
def my_function(str1, str2):
    print(f"Parameters are '{str1}' and '{str2}'")

my_function("123435", "44546")