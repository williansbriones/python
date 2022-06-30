import numpy as np
boleto=[]
nombrePasajero=[]
rut=[]
telefono=[]
banco=[]
compra=[nombrePasajero,rut,telefono,banco]
###########################################################################################
def menu():
    accion=int(input("Indique que accion decea realizar\n1)asientos disponibles\n2)comprar boletos\n3)anular vuelos\n4)Modificar datos de pasajero\n5)salir"))
    while True:
            if accion<0 or accion>5:

                accion=int(input("Indique una accion correcta\n1)asientos disponibles\n2)comprar boletos\n3)anular vuelos\n4)Modificar datos de pasajero\n5)salir"))
            else:
                break
    return(accion)
def arrays():
    acum=0
    asientos_normal=np.ones([5,6],dtype="int32")
    for i in range(5):
        for e in range(6):
            asientos_normal[i][e]=asientos_normal[i][e]+acum
            acum=acum+1
    asientos_vip=np.ones([2,6],dtype="int32")
    for i in range(2):
        for e in range(6):
            asientos_vip[i][e]=asientos_vip[i][e]+acum
            acum=acum+1
    total_asientos_n=np.concatenate((asientos_normal,asientos_vip),axis=0,dtype="int32")
    total_asientos=np.concatenate((asientos_normal,asientos_vip),axis=0,dtype="str")
    return(total_asientos,total_asientos_n)
def disponibles_num(total_asientos,total_asientos_n):
    tabla=""
    acum_c=0
    for i in range(7):
        for e in range(6):
            acum_c=acum_c+1
            if total_asientos[i][e].isnumeric():
                numero=total_asientos_n[i][e]
                
                if numero < 10:
                    tabla=tabla + "| "+ total_asientos[i][e]
                if numero > 9:
                    tabla=tabla + "|"+ total_asientos[i][e]
            else:
                tabla=tabla + "| "+ total_asientos[i][e]
            if acum_c==6:
                acum_c=0
                tabla=tabla + "\n"
    print(tabla)
    return(tabla)
def compra_fun(total_asientos,total_asientos_n,check):
    c=disponibles_num(total_asientos, total_asientos_n)
    compra_us=input("que asiento dacea comprar")
    cont_com=0
    while True:
        for i in range(5):
            for e in range(6):
                if total_asientos[i][e]==compra_us:
                    cont_com=1
                if cont_com==1:
                    total_asientos[i][e]="x"
                        break
        compra_us=input("indique un asiento valido")
       

        
                    
        
    
###########################################################################################
a,b=arrays()

###########################################################################################
while True:
    d=menu()
    a[0][5]="x"
    if d==1:
        c=disponibles_num(a,b)
        input("ENTER..................")
    if d==2:
        com=compra_fun(a,b,compra)