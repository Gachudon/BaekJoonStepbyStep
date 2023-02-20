import sys
input=sys.stdin.readline
n = int(input())
for i in range(n):
    m=i
    for j in str(i):
        m+=int(j)
    if m==n:
        print(i)
        quit()
print(0)