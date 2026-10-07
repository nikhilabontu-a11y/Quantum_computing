import numpy as np
ket0=np.array([1,0])
ket1=np.array([0,1])

output_0=ket1
output_1=ket0

m=np.column_stack([output_0,output_1])
print(m)