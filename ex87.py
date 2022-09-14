import math
matriz=[[0,0,0],[0,0,0],[0,0,0]]
lp=[]
lt=[]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input("Digite um número:"))
        if matriz[l][c]%2==0:
            lp.append(matriz[l][c])
    if c==2:
        lt.append(matriz[l][c])
print("-="*30)
print(matriz[0])
print(matriz[1])
print(matriz[2])
print("-="*30)

print(f'A soma dos valores pares é {sum(lp)}.')
print(f'A soma dos valores da terceira coluna é {sum(lt)}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')




