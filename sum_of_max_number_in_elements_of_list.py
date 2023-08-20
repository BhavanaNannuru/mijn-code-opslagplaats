n=int(input())
l=list(input().split())
if n==len(l):
    sum=0
    for i in l:
        sum+=max(list(map(int,list(i))))
    print(sum)

