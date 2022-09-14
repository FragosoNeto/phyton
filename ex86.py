l0=[[],[],[]]
l1=[[],[],[]]
l2=[[],[],[]]
c=0
c1=0
c2=-0
for n in range(0,3):
    n=int(input(f"Digite um valor para [0,{c}]:"))
    l0[c].append(n)
    c=c+1
for x in range(0,3):
    x = int(input(f"Digite um valor para [1,{c1}]:"))
    l1[c1].append(x)
    c1 = c1 + 1
for z in range(0,3):
    z = int(input(f"Digite um valor para [2,{c2}]:"))
    l2[c2].append(z)
    c2 = c2 + 1
print(l0)
print(l1)
print(l2)