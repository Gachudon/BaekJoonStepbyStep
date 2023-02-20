h, m = map(int,input().split())
if h>23 or h<0 or m>59 or m<0: quit()
t = int(input())
if t>1000 or t<0:quit()
m += t
while m >=60:
    h+=1
    if h==24: h=0
    m-=60
print("%d %d" % (h,m))