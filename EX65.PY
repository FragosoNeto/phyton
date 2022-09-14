c=0
n=1
l=[]
t='S'
while t=='S':
    n = int(input('DIGITE UM NÚMERO:'))
    l1 = l.append(n)
    c=c+1
    t=str(input('DESEJA CONTINUAL(S/N)')).upper().strip()[0]
    if t=='N':
        print(f'VOCÊ DIGITOU {c} NÚMEROS')
        s=sum(l)
        m=s/c
        print(f'A média entre eles é {m}')
        mx=max(l)
        min=min(l)
        print(f'O maior número é {mx}')
        print(f'O menor número é {min}')
print('FIM')


























































































































































