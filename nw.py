qcoca=150
qpeps=130
vcoca=1.50
vpeps=1.50
custo=2500

print("-"*30)
print("Faturamento com a venda de PEPSI")
print("-"*30)
fp=qpeps*vpeps
print(f'O faturamento de pepsi foi de R$ {fp:.2f}')

print('\n' + "-"*30)
print("Faturamento com a venda de COCA")
print("-"*30)
fp1=qcoca*vcoca
print(f'O faturamento de coca foi de R$ {fp1:.2f}')

print('\n' + "-"*30)
print("Lucro da Loja")
print("-"*30)
l=(fp+fp1)-custo
print(f'O lucro da loja foi de R$ {l:.2f}')