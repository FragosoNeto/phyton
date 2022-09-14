n=str(input('Digite uma expressão:')).strip().upper()
l=[]
for s in n:
    if s=='(':
        l.append('(')
    elif s==')':
        if len(l)>0:
            l.pop()
        else:
            l.append(')')
            break
print(l)









