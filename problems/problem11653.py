n=int(input())
if n>10000000 or n<1:quit()

while(n>1):
    for i in range(2,n+1):
        if n%i==0:
            print(i)
            n=int(n/i)
            break