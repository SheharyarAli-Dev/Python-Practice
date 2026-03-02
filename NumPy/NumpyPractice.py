#Topic 01:
"""
import numpy as np;

a=[[0]*3 for i in range(3)];

for i in range(0,3):
    for j in range (0,3):
        a[i][j]=j;

a=np.array(a, dtype=int, ndmin=1);

print(a);

b=np.array([[1,2],[3,4]], dtype=float);

print(b);

c=np.array([1,2,3],dtype=float,ndmin=1);

print(c);
"""


#Topic 02:
import numpy as np

a=np.zeros((3,4), dtype=int);

print(a);

b=np.ones((2,2),dtype=float)

print(b);

c=np.full((3,3),67,dtype=float);
print(c);

d=np.empty((2,3),dtype=int);
print(d);

e=np.identity(3);
print(e);

f=np.eye(3,k=2)
print(f);