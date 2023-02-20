'''
1/1 1/2 2/1 3/1 2/2 1/3 1/4 2/3 3/2 4/1 5/1 4/2 3/3 2/4 1/5 1/6...
분자가 1이면 분모에 1 더하고 분모가 1이 될 때까지 분자 +1 분모 -1
분모가 1이면 분자에 1 더하고 분자가 1이 될 때까지 분자 -1 분모 +1
'''
# ary=[]
# ary.append([1,1])
# ary.append([1,2])

# x = int(input())
# if x>10000000 or x<1:quit()
# c=1
# m=1
# cnt=1
# while cnt<x:
#     if c==1:
#         m+=1
#         cnt+=1
#         if cnt==x:
#             print("%d/%d"%(c,m))
#             quit()
#         while m>1:
#             c+=1
#             m-=1
#             cnt+=1
#             if cnt==x:
#                 print("%d/%d"%(c,m))
#                 quit()
#     elif m==1:
#         c+=1
#         cnt+=1
#         if cnt==x:
#             print("%d/%d"%(c,m))
#             quit()
#         while c>1:
#             m+=1
#             c-=1
#             cnt+=1
#             if cnt==x:
#                 print("%d/%d"%(c,m))
#                 quit()
# print("%d/%d"%(c,m))

X=int(input())

line=1
while X>line:
    X-=line
    line+=1
    
if line%2==0:
    a=X
    b=line-X+1
else:
    a=line-X+1
    b=X
    
print(a, '/', b, sep='')

'''
코드 출처 :https://deokkk9.tistory.com/11
대각선으로 각 줄을 나눠서 보면
[1/1], [1/2, 2/1], [3/1, 2/2, 1/3], [1/4, 2/3, 3/2, 4/1] 이렇게 나타낼 수 있다. 
따라서, 입력받은 X를 1씩 늘려 가며 빼서 몇 번째 줄에 몇 번째 숫자인지 구하고
짝수번 째 줄인지 홀수번째 줄인지에 따라 분자, 분모의 숫자의 방향이
홀수 줄인 경우 분자는 내림차순, 분모는 오름차순이고,
짝수 줄인 경우 그 반대이다.
'''