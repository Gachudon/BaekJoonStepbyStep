h, m = map(int,input().split())
if h>23 or h<0 or m>59 or m<0: quit()
if m-45 <0:
    if h-1 <0:
        h=23
        m=60+m-45
    else:
        h-=1
        m=60+m-45
else:
    m-=45
print("%d %d" % (h,m))