s=input()
t=input()
sum1=sum(list(map(ord,s)))
sum2=sum(list(map(ord,t)))
print(chr(abs(sum1-sum2)))
