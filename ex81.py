l=[]

while True:
    n = int(input('Digite um número:'))
    t=str(input('Deseja continuar?(S/N)')).strip().upper()
    l.append(n)
    if t=="N":
        break
if 5 in l:
    print("tem")

else:
    print("não há")

a = len(l)
l.sort(reverse=True)
print(a)
print(l)




