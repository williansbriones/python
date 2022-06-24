import numpy as np
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

asientos=np.concatenate((asientos_normal,asientos_vip),axis=0,dtype="str")
#asientos_totales=np.concatenate((asientos_normal,asientos_vip),axis=0)
#asientos_totales=np.astype(str)
print(asientos)
for i in range(7):
    for e in range(6):
        asientos[i][e]="x"
print(asientos)
print(asientos_normal.dtype)