"""
Scrieți un decorator care să controleze cazul în care un argument e negativ-
daca da- printeaza ca e negativ, daca nu- executa functia.
"""

def deco_negative_flag(func):

    def wrapper(*args):
        for arg in args:
            if arg < 0:
                print(f"Found a negative parameter: {arg}")
                break
        else:
            func(*args)
    return wrapper

@deco_negative_flag
def my_function(v1, v2, v3, v4):
    print(f"My vars are v1={v1}, v2={v2}, v3={v3}, v4={v4}")

my_function(1, 2, 3, 5)