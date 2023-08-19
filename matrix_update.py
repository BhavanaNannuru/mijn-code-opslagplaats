n=int(input())
x=int(input())
mat=[]
for i in range(n):
    mat.append(list(map(int,input().split())))
max=0
for i in range(n):
    for j in range(n):
        ele=mat[i][j]
        k=0
        while k<=ele:
            k+=x
        if k>ele:
            k-=x
        mat[i][j]=k
        print(mat[i][j],end=' ')
    print()
        
    

