c=0
s=0
while True:
    n=int(input('Digite um número:'))
    if n==999:
        break
    c=c+1
    s=s+n

print(f'Você digitou {c} e a soma deles é {s}')