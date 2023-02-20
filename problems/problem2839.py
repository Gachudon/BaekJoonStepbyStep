n=int(input())
if n>5000 or n<3:quit()
if n==4 or n==7:
    print(-1)
elif n%5==1:
    print(2+int((n-6)/5))
elif n%5==2:
    print(4+int((n-12)/5))
elif n%5==3:
    print(1+int((n-3)/5))
elif n%5==4:
    print(3+int((n-9)/5))
else:
    print(int(n/5))