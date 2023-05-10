from time import sleep
from datetime import  datetime
#
#
# #decorator pentru a rula functii doar la un anumit interval orar
# def decorator_interval(func):
#     def wrapper():
#         hour_now = datetime.now().hour
#         if hour_now >= 7 and hour_now < 19:
#             func()
#         else:
#             print("Outside time interval")
#     return wrapper
#
# @decorator_interval
# def fa_ceva():
#     sleep(2)
#     print("Fac ceva")
#
# def fa_ceva_fara_decorator():
#     hour_now = datetime.now().hour
#     if hour_now >= 7 and hour_now < 19:
#         sleep(2)
#         print("Fac ceva")
#     else:
#         print("Outside time interval")
#
# def fa_altceva_fara_decorator():
#     hour_now = datetime.now().hour
#     if hour_now >= 7 and hour_now < 21:
#         sleep(2)
#         print("Fac altceva")
#     else:
#         print("Outside time interval")
#
# fa_ceva()
# fa_altceva_fara_decorator()

# def decorator_with_args(func):
#     def wrapper(*args):
#         hour_now = datetime.now().hour
#         print(f"Cu 3 ore in urma a fost ora {int(hour_now)-3}")
#         func(*args)
#         print(f"Peste 4 ore va fi ora {int(hour_now)+4}")
#     return wrapper
# @decorator_with_args
# def my_function(v1, v2, v3):
#     print(f"Variabilele sunt {v1}, {v2}, {v3}")
#
# def decorator_1etaj(var1, var2):
#     def decorator_2etaj(func):
#         def wrapper(*args):
#             print(f"Variabilele 1e sunt {var1} & {var2}")
#             return func(*args)
#         return wrapper
#     return decorator_2etaj
#
# @decorator_1etaj(45,59)
# def functia_mea(a,b,c):
#     print(f" Variabile ale functiei decorate: {a},{b},{c}")
#
# #"Ion", "Elena", "Vasile"
# functia_mea("Ion", "Elena", "Vasile")
#
# """
# Rezultatul apelarii functiei decorate cu decorator ce contine variabile este:
# Variabilele 1e sunt 45 & 59
# Variabile ale functiei decorate: Ion,Elena,Vasile
#
# Adica s-au folosit variabilele decoratorului cat si variabilele functiei decorate
# """
#
# class Studenti:
#     denumire_scoala = "SDA"
#     def __init__(self, varsta):
#         self.varsta = varsta
#
#     #staticmethod este un decorator prin care nu folosim deloc variabilele definite in clasa
#     #un fel de helper function independenta de clasa, dar care ajuta in interiorul clasei
#     @staticmethod
#     def adult_sau_copil(cati_ani):
#         if cati_ani >= 18:
#             return "Adult"
#         else:
#             return "Copil"
#
#     @property
#     def spune_ce_scoala(self):
#         return f"Scoala este {self.denumire_scoala}"

#Chaining decorators - decoram cu mai multi decoratori o functie
def primul_decorator(func):
    def wrapper(*args):
        print("Primul decorator")
        return func(*args)
    return wrapper

def doilea_decorator(func):
    def wrapper(*args):
        print("Al doilea decorator")
        return func(*args)
    return wrapper

@primul_decorator
@doilea_decorator
def printare_ceva(text_a):
    print(f"Printez ceva, anume = {text_a}")

printare_ceva("Ce mai faci?")

