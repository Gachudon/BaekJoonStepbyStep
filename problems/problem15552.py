import sys

t = int(sys.stdin.readline())
if t>1000000:quit()

sum = []
for i in range(t):
    a, b = map(int,sys.stdin.readline().split())
    if a>1000 or a<1 or b>1000 or b<1:quit()
    sum.append(a+b)

for i in range(t):
    print(sum[i])