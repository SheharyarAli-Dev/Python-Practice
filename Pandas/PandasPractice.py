#TOPIC 1
"""
import pandas as pd;

a=pd.Series([1,2,3], index=["a","b","c"])

print(a)
print(a["a"])

b=pd.Series([4,5,6], index=["d","e","f"]);

print(b);
print(b["e"])


c={
    "a":1,
    "b":2,
    "c":3
}

d=pd.Series(c)
print(d[["a","c"]])
print(b[["d","f"]])
"""
#TOPIC 2
"""
import pandas as pd

a=pd.Series([1,2,3], index=["a","b","c"], name="Scores");

print(a);
print(a["a"])
print(a[["a","c"]])
print(a.index)
print(a.values)
print(a.dtype)
print(a.name)
"""

#TOPIC 3
"""
import pandas as pd
import numpy as np

a=[
    [1,2,3],
    [4,5,6]
]
print(pd.DataFrame(a, columns=[0,1,2]))

b={
    "Name":["Ali","Baqir","Carol"],
    "Age":[1,2,3]
}
print(pd.DataFrame(b))

c=np.array([[1,2],[3,4]]);

d=pd.DataFrame(c,columns=["First","Second"]);

print(d)

e=pd.read_csv("Pandas/test.csv")
print(e)
"""

#TOPIC 4:
"""
import pandas as pd

a=pd.read_csv("Pandas/test.csv",usecols=["Name"])
print(a)

a.to_csv("Output.csv",index=False)
a=pd.read_excel("Pandas/check.xlsx", engine="openpyxl");
print(a)

#pd.read_csv(file, sep=",", header=0) IMPORTANT
"""

#TOPIC 5:
"""
import pandas as pd

d={
    "a":[1,2,3],
    "b":[4,5,6]
}
a=pd.DataFrame(d,index=["1","2","3"])
print(a);
"""

#TOPIC 6:
"""
import pandas as pd
a=pd.read_csv("Pandas/test.csv")
print(a)
print()
print(a.head(6))
print()
print(a.tail())
c=a.head()
c.to_csv("Ouput.csv",index=False)
print();
print(a.sample(3))
print()
print(a.shape)
print()
print(a.info())
print()
print(a.describe())
print()
print(a.dtypes)
print()
print(a["Marks"].value_counts())
print()
"""

#TOPIC 7:
"""
import pandas as pd

a=pd.read_csv("Pandas/test.csv")
print(a[["Marks","Age"]])
print()
print(a.iloc[0:1])
print()
print(a)
print()
print(a[a["Marks"]<90])
print()
print(a["Age"])
print()
print(a.iloc[[0,2]])
"""

#TOPIC 8:
"""
import pandas as pd

a=pd.read_csv("Pandas/test.csv")
print(a.isnull())
print()
print(a.isna())
print()
print(a.notnull())
print()
print(a.isnull().sum())
print()
print(a[a["Age"].isnull()])
"""

#TOPIC 9:

import pandas as pd

a=pd.read_csv("Pandas/test.csv")
print(a.duplicated())
a=a.drop_duplicates()
print()
print(a.duplicated())

