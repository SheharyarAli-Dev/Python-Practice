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

import pandas as pd

a=pd.Series([1,2,3], index=["a","b","c"], name="Scores");

print(a);
print(a["a"])
print(a[["a","c"]])
print(a.index)
print(a.values)
print(a.dtype)
print(a.name)

