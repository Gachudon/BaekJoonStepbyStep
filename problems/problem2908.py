a, b = map(str,input().split())
if len(a)!=3 or len(b)!=3 or int(a)==int(b):quit()
for i in a:
    if i =='0':quit()
for i in b:
    if i =='0':quit()

a = a[::-1]
b = b[::-1]

if int(a)>int(b):print(a)
else:print(b)