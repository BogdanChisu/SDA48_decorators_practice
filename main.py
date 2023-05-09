# modalitare de a adauga functionalitati unei functii
"""
activarea unei functii intr-un anume interval de timp
date_wrapper
"""
# from time import sleep
# from datetime import datetime
#
# hour_now = datetime.now().hour
# print(hour_now)
#decorator pentru a rula functii doar la un anumit interval orar
# def decorator_interval(func):
#     def wrapper():
#
#         if hour_now >= 7 and hour_now < 18:
#             func()
#         else:
#             print("Outside specified interval")
#     return wrapper
#
# @decorator_interval
# def fa_ceva():
#     # sleep(2)
#     print("Fac ceva")
#
# def fa_ceva_fara_decorator():
#     # sleep(2)
#     if hour_now >= 7 and hour_now < 22:
#         print("fac_altceva")
#     else:
#         print("Outside specified interval")
#
# fa_ceva()
# fa_ceva_fara_decorator()

def decorator_with_args(func):

    def wrapper(*args):
        hour_now = datetime.now().hour
        print(f"Cu 3 ore in urma a fost ora {int(hour_now) - 3}")
        func(*args)
        print(f"Peste 4 ore va fi ora {int(hour_now) + 4}")
    return wrapper

def my_function(v1, v2, v3):
    print(f"Variabilele sunt {v1}, {v2}, {v3}")

@decorator_with_args
def my_function_2(v1, v2, v3):
    print(f"Variabilele sunt {v1}, {v2}, {v3}")
#
# my_function_2(1, 2, 3)

# def decorator_cu_etaj(var1, var2):
#
#     def decorator_2etaj(func):
#         def wrapper(*args):
#             print(f"Variabilele 1e ale decoratorului sunt {var1} & {var2}")
#             return func(*args)
#         return wrapper
#     return decorator_2etaj()
#
# @decorator_cu_etaj(45, 59)
# def functia_mea(v1, v2, v3):
#     print(f"Varibilele functie decorate sunt {v1} {v2} {v3}")
#
# functia_mea("Ion", "Elena", "Vasile")

# class Studenti:
#     def __init__(self, varsta):
#         self.varsta = varsta
#
#     # static method este un decorator prin care nu folosim deloc varibilele definite in clasa
#     # un fel de 'helper function', independenta de clasa
#     @staticmethod
#     def adult_sau_copil(self, cati_ani):
#         if cati_ani >= 18:
#             return "Adult"
#         else:
#             return "Copil"
#
#     @property
#     def spune_ce_scoale(self):
#         return f"Scoala este {self.denumire_scoala}"


# CHAINING DECORATORS
def primul_decorator(func):

    def wrapper(*args):
        print("Primul decorator")
        return func(*args)
    return wrapper

def al_doilea_decorator(func):
    def wrapper(*args):
        print("Al doilea decorator")
        return func(*args)
    return wrapper
@primul_decorator
@al_doilea_decorator
def printare_Ceva(text_a):
    print(f"Printez ceva {text_a}")

printare_Ceva("Ce mai faci?")

