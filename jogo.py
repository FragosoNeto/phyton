import random
l=[0,1,2,3,4,5,6,7,8,9,10]
k=random.choice(l)
print(k)
x=[0,1,2,3,4,5,6,7,8,9,10]
p=0
while k!=x:
    x=int(input('Pense em um número entre 0 e 10:'))
    if k>x:
        a=print('Seu numero é inferior ao do computador, tente novalente!')
    elif x>k:
        a = print('Seu número é superior ao do computador, tente novalente!')
    p=p+1
print(f'{p} palpites')
print('Parabéns, você acertou')



