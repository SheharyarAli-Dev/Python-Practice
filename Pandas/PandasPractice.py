import pandas as pd;

a=pd.Series([1,2,3], index=["a","b","c"])

print(a)
print(a["a"])

b=pd.Series([4,5,6], index=["d","e","f"]);

print(b);
print(b["e"])