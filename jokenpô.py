import random
import time

lista=[1,2,3]
cp=int(random.choice(lista))
time.sleep(1)
print('''===VAMOS JOGAR ===
JO
KEN
PÔ''')
time.sleep(1)
print('='*20)
time.sleep(1)
n1=print('1-Pedra')
time.sleep(1)
n2=print('2-Papel')
time.sleep(1)
n3=print('3-Tesoura')
time.sleep(1)
n=int(input('INFORME SUA OPÇÃO:'))
if cp==n:
    print('HOUVE UM EMPATE')
elif n==1 and cp==3:
    print('VOCÊ VENCEU, O COMPUTADOR USOU TESOURA E VOCÊ PEDRA!')
elif n==3 and cp==2:
    print('VOCÊ VENCEU, O COMPUTADOR USOU PAPEL E VOCÊ TESOURA!')
elif n==2 and cp==1:
    print('VOCÊ VENCEU, O COMPUTADOR USOU PEDRA E VOCÊ PAPEL!')
elif cp==1 and n==3:
    print('O COMPUTADOR VENCEU, O COMPUTADOR USOU PEDRA E VOCÊ TESOURA!')
elif cp==3 and n==2:
    print('O COMPUTADOR VENCEU, O COMPUTADOR USOU TESOURA E VOCÊ PAPEL')
elif n == 1  and cp == 2:
    print('VOCÊ VENCEU, O COMPUTADOR USOU PAPEL E VOCÊ PEDRA')
else:
    print('OPÇÃO INVÁLIDA')
