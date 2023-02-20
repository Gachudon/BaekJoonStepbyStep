'''
코드 출처: https://hongcoding.tistory.com/39

문제 설명
스택에 수를 push할 때는 반드시 오름차순으로만 push할 수 있다.
그리고 스택을 쌓다가 필요한 타이밍에 pop을 하게 되는데, 이 pop을 한 수들을 쭉
나열했을 때, N줄에 걸쳐 입력한 수열과 같아야 한다.
즉, 예제로 N=8이고 다음 줄 부터 4,3,6,8,7,5,2,1을 입력한 상황을 예로 들어보면
내가 스택을 쌓다가 중간에 한 번씩 pop을 한 데이터들을 나열한 순서도
4,3,6,8,7,5,2,1이 되어야 한다는 것이다.

풀이 과정
위의 예제들을 예로 들어 설명하면, 처음으로 4를 입력했다. 즉, 내가 첫 번째로
pop한 숫자가 4가 되어야 한다. 그러기 위해서는 1,2,3,4가 이미 스택안에 있어야
한다. 그래서 입력한 수를 만날 때 까지는 계속 push를 해서 1,2,3,4가 스택에
있도록 해야한다.

그리고 나서 4를 꺼내 스택은 현재 1,2,3인 상황이다.
그 다음으로 3이 주어졌기 때문에 push없이 현재 스택에서 pop을 하면 된다. 그리고
스택은 1,2가 된다. 그 다음 입력으로 6이 주어졌기 때문에, 다시 6을 만날 때 까지
이전의 숫자들을 push 해준다.(즉 5,6 push)

이 때, stack에서 pop할 숫자(TOP) 가 입력한 숫자가 아닐 경우(작을 경우) 정답을
완성할 수 없다. 왜냐하면 TOP값이 입력한 숫자보다 크면, 입력한 수를 꺼내기 위해
계속 POP을 애햐 하기 때문에 그 과정에서 POP한 수들의 수열이 정답과 일치하지
않게 되기 때문이다.
'''

from sys import stdin
input=stdin.readline

n=int(input())
stack=[]
answer=[]
flag=0
cur=1
for i in range(n):
    num=int(input())
    while cur<=num: # 입력한 수를 만날 때 까지 오름차순으로 push
        stack.append(cur)
        answer.append('+')
        cur+=1
    # 입력한 수를 만나면 while문 탈출, 즉 cur=num일 때 까지 while문을 돌아 스택을 쌓는다.

    if stack[-1]==num: # stack의 TOP이 입력한 숫자와 같다면
        stack.pop() # 스택의 TOP을 꺼내 수열을 만들어 준다.
        answer.append('-')
    else: # stack의 TOP이 입력한 수가 아니면 주어진 스택을 만들 수 없다.
        print('NO') # 왜냐하면 12345 처럼 오름차순으로 스택이 입력되는데
        flag=1 # TOP이 num보다 크면 num은 TOP보다 더 아래에 쌓여있기 때문이다.
        break
if flag==0:
    for i in answer:
        print(i)

# from sys import stdin
# input=stdin.readline

# n=int(input())
# arr=[0]*n
# stack=[]
# log=''
# is_available=True
# j=1
# for i in range(n):
#     arr[i]=int(input())
#     if not is_available:continue
#     while True:
#         if len(stack)<1:
#             stack.append(j)
#             j+=1
#             log+='+'
#         if stack[-1]<arr[i]:
#             stack.append(j)
#             j+=1
#             log+='+'
#         elif stack[-1]==arr[i]:
#             stack.pop()
#             log+='-'
#             break
#         else:
#             is_available=False

# if not is_available:print('NO')
# else:
#     for i in log:
#         print(i)