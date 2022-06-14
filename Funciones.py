#sin argumentos y sin retornos
def saludar():
    print("hola")
saludar()
#sin argumento y con retornos
def sumar():
    a=int(input("indique un numero"))
    b=int(input("indique un numero"))
    c=a+b
    return c
s= sumar()
print (s)
#con argumento y sin retornos
def resta(d,t):
    c=d+t
    print(f"la suma de {d} + {t} = {c}")

d=int(input("indique un numero"))
t=int(input("indique un numero"))
resta(d,t)
#con argumento y con retornos
def suma1(q,w):
    return q+w
g=int(input("indique un numero"))
h=int(input("indique un numero"))
s=suma1(g,h)
print(s)
#Cuando se ingresan varios datos
def varios(*args):
    print(type(args))
varios(1,5,"fdaf")