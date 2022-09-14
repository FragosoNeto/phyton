s = str(input('Informe seu sexo:')).upper().strip()
while s not in "MmFf":
    print('Sexo inválido')
    input('Informe seu sexo:')
print(f'sexo {s}, registrado com o sucesso')




