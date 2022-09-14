n=0
c=0
l=[]
while n!=999:
   n = int(input('Digite um número, sabendo que 999 para o sistema:'))
   l1 = l.append(n)
   c=c+1
   if n==999:
      s=sum(l)
      s1=s-999
      print(s1)
print('FIM')