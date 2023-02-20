n=int(input())
if n>100 or n<1:quit()
for i in range(n):
    for j in range(n-i-1):
        print(" ",end='')
    for j in range(i+1):
        print("*",end='')
    print()