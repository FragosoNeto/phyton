l=list()
g=list()
mai=men=0
while True:
    n=str(input('Nome:'))
    i=float(input('peso:'))
    g.append(n)
    g.append(i)
    if len(l) == 0:
        mai=men=g[1]
    else:
        if g[1]>mai:
            mai=g[1]
        elif g[1]<men:
            men=g[1]
    l.append((g[:]))
    h = str(input('DESEJA CONTINUAR:(S/N)')).upper()
    g.clear()
    if h in 'Nn':
        break

print(mai)
print(men)




