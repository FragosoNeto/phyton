mat=[]
cont=0
while True:
    nome = str(input('Nome:'))
    n1 = float(input('Nota 1:'))
    n2 = float(input('Nota 2:'))
    for l in range(cont, 4):
        for c in range(cont, 4):
            s = input("Deseja continuar?[S/N]").strip().upper()[0]
            mat.append(nome)
            mat.append(n1)
            mat.append(n2)
            if s in 'Nn':
                break

print(mat)