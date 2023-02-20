'''
코드 출처: https://hooongs.tistory.com/114
./problem1629.py에서 거듭제곱을 분할정복으로 풀었었다. 이 문제도 이 로직을
그대로 2차원 배열에 적용을 하면 풀 수 있다.
처음에 행렬은 곱하는 순서가 상관이 있다는 것을 생각하고는 분할 정복을 하면
안된다고 생각을 했지만 직접 계산해보니 n*n의 같은 행렬들을 계속 곱해주는 거라
순서가 상관이 없다는 것을 알아채고는 위에서 말한 것 처럼 2분할을 해가면서
거듭제곱을 구할 수 있었다.
2분할 하는 메서드와 행렬곱셈을 하는 메서드를 만들면 되고 수가 커질 수 있기
때문에 중간 중간 1000으로 나누어 주어야 하는 데 행렬곱셈을 해줄 때 원소
한개의 계산을 끝낼 때 마다 1000으로 나눈 나머지를 저장해준다. 필자가 이렇게
풀고 계속 틀렸습니다 가 나왔는데, 문제는 마지막 출력을 해줄 때 1000으로 모듈라
연산을 안 해 주었다.
'''

def mul(n,matrix1,matrix2):
    result=[[0 for _ in range(n)]for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j]+=matrix1[i][k]*matrix2[k][j]
            result[i][j]%=1000

    return result

def devide(n,b,matrix):
    if b==1:
        return matrix
    elif b==2:
        return mul(n,matrix,matrix)
    else:
        tmp=devide(n,b//2,matrix)
        if b%2==0:
            return mul(n,tmp,tmp)
        else:
            return mul(n,mul(n,tmp,tmp),matrix)
        
n,b=map(int,input().split())
a=[list(map(int,input().split()))for _ in range(n)]

result=devide(n,b,a)
for row in result:
    for num in row:
        print(num%1000,end=' ')
    print()