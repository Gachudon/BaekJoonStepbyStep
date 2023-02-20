n,m = map(int,input().split())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))
    if len(matrix[i])!=m:quit()
matrix1=[]
for i in range(n):
    matrix1.append(list(map(int,input().split())))
    if len(matrix1[i])!=m:quit()

for i in range(n):
    for j in range(m):
        matrix[i][j]+=matrix1[i][j]
        print("%d "%matrix[i][j],end='')
    print()