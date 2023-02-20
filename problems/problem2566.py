matrix=[]
max=0
maxx=0
maxy=0
for i in range(9):
    matrix.append(list(map(int,input().split())))
    if len(matrix[i])!=9:quit()
    for j in range(9):
        if matrix[i][j]>99 or matrix[i][j]<0:quit()
        if max<matrix[i][j]:
            max=matrix[i][j]
            maxx=i
            maxy=j
print(max)
print("%d %d"%(maxx+1,maxy+1))