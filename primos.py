import numbers
import math
p=0
n=int(input('Digite um número:'))
for i in range(1,n+1):
    if n % i ==0:
        p+=1
if p==2:
    print("O número é primo")
else:
    print('Não é primo')








