"""
Scrieti un decorator care sa scrie restul impartirii lui a la b (ambele sunt argumente ale
functiei decorate)
"""
def a_mod_b(func):

    def wrapper(*args):
        func(*args)
        print(f"a_mod_b = {args[0] % args[1]}")
    return wrapper

@a_mod_b
def functia_mea(var1, var2):
    print(f"Numerele sunt a={var1} si b={var2}")

functia_mea(3, 5)

