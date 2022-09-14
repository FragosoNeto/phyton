l=[]
lp=[]
li=[]
cont=0
for c in range(0,6):
    c=int(input('Digite um número:'))
    l.append(c)
    cont=cont+1
    if c%2==0:
        lp.append(c)
    else:
        li.append(c)
s=l+lp+li
print(l)
print(lp)
print(li)

print(s)
