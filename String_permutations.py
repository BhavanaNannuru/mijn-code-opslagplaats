import itertools
str=input()
p=list(itertools.permutations(str))
per=[]
n=['0','1','2','3','4','5','6','7','8','9']
for l in p:
    if l[0] in n:
        continue
    else:
        per.append(''.join(l))
per.sort()
for i in per:
    print(i,end=' ')
