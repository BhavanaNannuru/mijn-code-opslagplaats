def prints(mat):
    row=len(mat)
    column=len(mat[0])
    for i in range(row):
        for j in range(column):
            print(mat[i][j],end=' ')
        print()
    print()
row1=int(input("Enter the number of rows:"))
column1=int(input("Enter the number of columns:"))
mat1=[]
mat2=[]
print("Enter the values for mat1:")
for i in range(row1):
    a=[]
    for j in range(column1):
        a.append(int(input("Enter the element")))
    mat1.append(a)

print("Enter the values for mat2:")
row2=int(input("Enter the number of rows:"))
column2=int(input("Enter the number of columns:"))
for i in range(row2):
    a=[]
    for j in range(column2):
        a.append(int(input("Enter the element: ")))
    mat2.append(a)
prints(mat1)
prints(mat2)

        
while True:
    opt=int(input("Enter\n1for addition\n2 for subtraction\n3 for multiplication\nAnything else for exit"))
    if opt==1:
        if row1==row2 and column1==column2:
            for i in range(row1):
                for j in range(column1):
                    print(mat1[i][j]+mat2[i][j],end=' ')
                print()
    elif opt==2:
        if row1==row2 and column1==column2:
            for i in range(row1):
                for j in range(column1):
                    print(mat1[i][j]-mat2[i][j],end=' ')
                print()
    elif opt==3:
        if column1==row2:
            result=[]
            for i in range(row1):
                a=[]
                for j in range(column2):
                    a.append(0)
                result.append(a)
        
            for i in range(len(mat1)):
                for j in range(len(mat2[0])):
                    for k in range(len(mat2)):
                        result[i][j]+=mat1[i][k]*mat2[k][j]
        prints(result)
            
    else:
        break

        
        
            
            
    
