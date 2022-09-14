n1=int(input('Digite o primeiro número de uma PA:'))
r=int(input('Digite a razão de uma PA:'))
nn=int(input('Digite o número de termos de uma PA:'))
nt=n1+(nn-1)*r
y=1
t=n1
mais=nn
total=0
while mais != 0:
    total = total + mais
    while y<=total:
        print(t)
        y = y + 1
        t = t + r
    mais=int(input('Digite o número de termos de uma PA:'))






