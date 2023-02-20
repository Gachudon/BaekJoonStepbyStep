n = int(input())
if n>10000 or n<1 : quit()
sum =0
for i in range(n+1):
    sum+=i
print(sum)