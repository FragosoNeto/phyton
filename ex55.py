import pandas as pd

s=[]
for i in range(0,6):
    p=f1loat(input('Qual o seu peso em kg:'))
    s.append(p)
print(s)
a=pd.Series(s)
d=a.max()
e=a.min()
print(d)
print(e)

