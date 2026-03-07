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

"""
#Topic 02:
import numpy as np

a=np.zeros((3,4), dtype=int);

print(a);

b=np.ones((2,2),dtype=float)

print(b);

c=np.full((3,3),3,dtype=float);
print(c);

d=np.empty((2,3),dtype=int);
print(d);

e=np.identity(3);
print(e);

f=np.eye(3,k=2)
print(f);
"""

#Topic 3
"""
import numpy as np

a=np.arange(0,50,10);
print(a);

b=np.linspace(0,10,100,endpoint=True);
print(b);

c=np.logspace(3,5,10);
print(c);

d=np.geomspace(10,100,4);
print(d);
"""

#Topic 3
"""
import numpy as np;

a=np.array([1,2,3],dtype=np.float32);
print(a);

b=np.array([[1,2,4]],dtype=np.bool_);
print(b);
b.astype(np.int32);
print(b);

print(b.ndim);
print(b.shape);
print(b.size);
print(b.itemsize);
"""


#Topic 4
"""
import numpy as np

a=np.array([1,2,3],dtype=np.int16,ndmin=1);
print(a[0:1]);

b=np.array([[1,2,3],[4,5,6]],dtype=np.int16,ndmin=1);
#print(b[1,2]);
#print(b[0,:]);
#print(b[1:2, 0:2]);
print(b.imag);
"""

#Topic 5
"""
import numpy as np

a=np.ones((3,3),dtype=np.int16);
print(a);

a=a.reshape(9,1);
print(a);

a=a.reshape(-1,3)
print(a);

a=a.flatten();
print(a);


b=np.array([1,2,3]);
print(b);
b=np.expand_dims(b,axis=0);
print(b);
"""


#Topic 6
"""
import numpy as np;

a=np.array([1,2,3]);
print(a);

a=np.expand_dims([1,2,3],axis=1);
print(a);

b=np.squeeze(([1],[2]));
print(b);
"""


#Topic 7:
"""
import numpy as np

a=np.array(([1,2],[3,4]), dtype=np.int32);
b=np.array(([5,6],[7,8]), dtype=np.int32);

c=np.concatenate((a,b),axis=1);
print(c);

d=np.vstack((a,b))
print(d);

e=np.column_stack((a,b));

print(e);
"""

#Topic 8:




