'''
코드 출처 : https://seongonion.tistory.com/103
백트래킹의 가장 기본 문제 중 하나인 N-Queen 문제이다.
처음에는 퀸이 놓인 위치를 기록해주기 위해서 2차원 배열을 사용하려 했으나 단순히
1차원 배열의 인덱스와 값을 통해서 위치를 기록해줄 수 있었다.
row[i]=j는 다음과 같이 해석될 수 있다.
"퀸을 [i,j]위치에 놓겠다."
퀸의 위치를 정하고 나서는, 해당 위치에 퀸을 놓을 수 있는지 없는지
is_promising 함수를 통해서 판단한다.
퀸을 놓지 못하는 경우는 2가지이다.
1) 같은 열에 다른 퀸이 있는 경우
2) 왼쪽 대각선, 오른쪽 대각선에 다른 퀸이 있는 경우

추가
해당 문제의 해당 코드는 Python으로는 통과가 안되고, pypy3로 제출 시
통과됩니다. 다만, 변수 선언 위치와 같은 사소한 것에 따라서도 통과/시간초과가
갈리기도 하는 말 그대로 파이썬으로 통과하기 정말 빡빡한 문제로 보입니다.
'''

n = int(input())

ans = 0
row = [0] * n

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):
                n_queens(x+1)

n_queens(0)
print(ans)