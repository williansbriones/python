import numpy as np
tabla=""
acum=0
acum_c=0
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
print(total_asientos)
total_asientos[1][1]="x"
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