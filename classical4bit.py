import numpy as np
ket0=np.array([1,0])
ket1=np.array([0,1])

kron00 =np.kron(ket0,ket0)#1000
kron01 =np.kron(ket0,ket1)#0100
kron10 =np.kron(ket1,ket0)#0010
kron11 =np.kron(ket1,ket1)#0001

#ips--ops
# 00--01
# 01--11
# 11--00
# 10--11


m=np.column_stack((kron00,
                   kron01,
                   kron11,
                   kron10))
print(m)