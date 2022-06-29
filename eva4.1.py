import numpy as np
acum_c=0
acum=0
comprador=[]
numero_com=[]
fecha=[]
alto=[]
largo=[]
ticket=[comprador,numero_com,fecha,alto,largo]
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
total_asientos=np.concatenate((asientos_normal,asientos_vip),axis=0,dtype="str")
print(total_asientos)
def menu():
    accion=int(input("Indique que accion decea realizar\n1)asientos disponibles\n2)comprar boletos\n3)anular vuelos\n4)Modificar datos de pasajero\n5)salir"))
    while True:
            if accion<0 or accion>5:

                accion=int(input("Indique una accion correcta\n1)asientos disponibles\n2)comprar boletos\n3)anular vuelos\n4)Modificar datos de pasajero\n5)salir"))
            else:
                break
    return(accion)
while True:   
    a=menu()
    tabla1=""
    if a==1:
        for i in range(7):
            for e in range(6):
                acum_c=acum_c+1
                if True:
                    numero=total_asientos[i][e]
                    eliminar=".0"
                    for x in range(len(eliminar)):
                        numero = numero.replace(eliminar[x],"")
                        int=numero
                    print(numero)
                elif numero < 10:
                        str=numero
                        tabla1=tabla1+"| "+numero
                elif numero > 9:
                        str=numero
                        tabla1=tabla1+"|"+numero
                else:
                    tabla1=tabla1+"| "+total_asientos[i][e]
                if acum_c==6:
                    acum_c=0
                    tabla1=tabla1 + "\n"
    print(tabla1)
    input("enter")
    if a==2:
        comprar=input("Que asiento decea comprar")

    if a==3:
        pass
    if a==4:
        pass
    if a==5:
        break
print("Gracias por comprar en vuelos DUOC UC")
