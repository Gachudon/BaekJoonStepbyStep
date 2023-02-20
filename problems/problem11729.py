# 한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
# 쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.
# import sys

# input=sys.stdin.readline

# def hanoi(n:int):
#     if n==1:return 1
#     else: return 1 + 2*hanoi(n-1)

# def printHow(n:int,f=1,t=3):
#     if n==1: print(f,t)
#     elif f==1 and t==3:
#         printHow(n-1,1,2)
#         print(f,t)
#         printHow(n-1,2,3)
#     elif f==1 and t==2:
#         printHow(n-1,1,3)
#         print(f,t)
#         printHow(n-1,3,2)
#     elif f==2 and t==1:
#         printHow(n-1,2,3)
#         print(f,t)
#         printHow(n-1,3,1)
#     elif f==2 and t==3:
#         printHow(n-1,2,1)
#         print(f,t)
#         printHow(n-1,1,3)
#     elif f==3 and t==1:
#         printHow(n-1,3,2)
#         print(f,t)
#         printHow(n-1,2,1)
#     elif f==3 and t==2:
#         printHow(n-1,3,1)
#         print(f,t)
#         printHow(n-1,1,2)

# m=int(input())
# print(hanoi(m))
# printHow(m)



def hanoi_tower(n, start, end) :
    if n == 1 :
        print(start, end)
        return
       
    hanoi_tower(n-1, start, 6-start-end) # 1단계
    print(start, end) # 2단계
    hanoi_tower(n-1, 6-start-end, end) # 3단계
    
n = int(input())
print(2**n-1)
hanoi_tower(n, 1, 3)

'''
코드 출처: https://study-all-night.tistory.com/6
start 막대에서 6-start-end 막대로 옮겼는데 start 막대에 있는 n개의 원판 중
n-1개의 원판을 end 막대가 아닌 2번 막대로 옮기는 것을 보실 수 있습니다.
그런데 우리는 start와 end 막대의 번호만을 알고 있을 뿐 나머지 막대의 번호는
알지 못합니다! 그러나!! 우리는 start막대와 end막대 그리고 번호 모를 막대의
번호를 다 합치면 6이 된다는 사실(1+2+3)을 알고있으므로
결국, 6에서 start와 end를 빼주면 번호 모를 막대의 번호를 알게 되는 것이죠!
'''