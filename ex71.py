t = int(input('DESEJA SACAR QUANTO?:(R$)'))
total=t
tc=0
c=50
cont=0
while True:
    if t>=c:
        t=t-c
        tc=tc+1
    else:
        if t<c:
           c=20
           t = t - c
           tc = tc + 1
    break
    print(tc)









