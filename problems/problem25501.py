import sys

def recursion(s:str,l:int,r:int,cnt=1):
    if l>=r:return 1, cnt
    elif s[l] != s[r]:return 0, cnt
    else:return recursion(s,l+1,r-1,cnt+1)

def isPalindrome(s:str):
    return recursion(s,0,len(s)-1)

n=int(input())
if n>1000 or n<1:quit()
result=[None]*n
for i in range(n):
    result[i]=isPalindrome(sys.stdin.readline().replace('\n',''))

for i in result:
    print("%d %d"%i)