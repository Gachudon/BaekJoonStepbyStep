n=int(input())
queue=[i for i in range(1,n+1)]
top=0
bottom=len(queue)-1

while abs(bottom-top)>=1:
    top=(top+1)%n
    bottom=(bottom+1)%n
    queue[bottom]=queue[top]
    top=(top+1)%n

print(queue[bottom])