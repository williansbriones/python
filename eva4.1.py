import numpy as np
import os
acum=0
asientos_normal=np.ones([5,6])
for i in range(5):
    for e in range(6):
        asientos_normal[i][e]=asientos_normal[i][e]+acum
        acum=acum+1
    
asientos_vip=np.ones([2,6])
for i in range(2):
    for e in range(6):
        asientos_vip[i][e]=asientos_vip[i][e]+acum
        acum=acum+1
total_asientos=np.concatenate((asientos_vip,asientos_normal),axis=0)
def menu():
    os.system(clear)
    accion=int(input("Indique que accion decea realizar\n1)asientos disponibles\n2)comprar boletos\n3)anular vuelos\n4)Modificar datos de pasajero\n5)salir"))
    while True:
            if accion<0 or accion>5:

                accion=int(input("Indique una accion correcta\n1)asientos disponibles\n2)comprar boletos\n3)anular vuelos\n4)Modificar datos de pasajero\n5)salir"))
            else:
                os.system(clear)
                break
    return(accion)
while True:   
    a=menu()
    if a==1:
        print(asientos_normal)
        print("____________________________")
        print(asientos_vip)
        input("enter para continuar.....")

    if a==2:
        pass
    if a==3:
        pass
    if a==4:
        pass
    if a==5:
        break
print("Gracias por comprar en vuelos DUOC UC")
