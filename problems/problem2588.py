a = int(input())
if a> 999 or a <100:
    quit()

b = int(input())
if b> 999 or b <100:
    quit()
c = a*b
for i in range(0,3):
    print(a*(b%10))
    b= int(b/10)
print(c)