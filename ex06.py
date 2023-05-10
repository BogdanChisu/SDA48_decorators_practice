"""
Scrieți un decorator care să controleze cazul în care un argument e negativ-
daca da- printeaza ca e negativ, daca nu- executa functia.
"""

def deco_negative_flag(func):

    def wrapper(*args):
        func(*args)
        for arg in args:
            if (not isinstance(arg, int)) and (not isinstance(arg, float)):
                print(f"{arg} is not valid.")
                continue
            elif arg < 0:
                print(f"Found a negative parameter: {arg}")

    return wrapper

@deco_negative_flag
def my_function(*args):
    print(f"My vars are {args}")

my_function(1, 2, 3, -5, "woeiuy", 7.4)