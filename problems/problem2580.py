'''
#include <iostream>
using namespace std;

int a[10][10];
bool c[10][10];
bool c2[10][10];
bool c3[10][10];
int n=9;
int cnt=0;

int square(int x, int y) {
    return (x/3)*3+(y/3);
}

bool go(int z) {
    cnt += 1;
    if (cnt >= 10000000) {
        return true;
    }
    if (z == 81) {
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                cout << a[i][j] << ' ';
            }
            cout << '\n';
        }
        return true;
    }
    int x = z/n;
    int y = z%n;
    if (a[x][y] != 0) {
        return go(z+1);
    } else {
        for (int i=1; i<=9; i++) {
            if (c[x][i] == 0 && c2[y][i] == 0 && c3[square(x,y)][i]==0) {
                c[x][i] = c2[y][i] = c3[square(x,y)][i] = true;
                a[x][y] = i;
                if (go(z+1)) {
                    return true;
                }
                a[x][y] = 0;
                c[x][i] = c2[y][i] = c3[square(x,y)][i] = false;
            }
        }
    }
    return false;
}

int main() {
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cin >> a[i][j];
            if (a[i][j] != 0) {
                c[i][a[i][j]] = true;
                c2[j][a[i][j]] = true;
                c3[square(i,j)][a[i][j]] = true;
            }
        }
    }

    go(0);
    return 0;
}

코드 출처: https://www.acmicpc.net/problem/12095
'''

# import sys
# input=sys.stdin.readline

# sudoku=[None for j in range(9)]
# for i in range(9):
#     sudoku[i]=list(map(int,input().split()))

# for i in range(9):
#     for j in range(9):
#         w=[]
#         l=[]
#         s=[]
#         if(sudoku[i][j]==0):

'''
코드 출처 :https://hongcoding.tistory.com/118
맵이 주어졌을 때 첫 번째 빈 칸부터 시작하여 마지막 빈 칸까지 적절한 수를
넣어가며 스도쿠를 완성시켜야 한다. 그래서 DFS+백트래킹을 통해 첫 번째 칸에
1~9 숫자를 넣어가며 확인하면 된다.
풀이방법은 다음과 같다.

먼저 문제의 빈 칸은 0으로 주어지기 때문에 graph의 0인 칸의 위치정보(x,y)를
blank 리스트에 넣어준다.

첫 번째 빈칸에 1~9까지의 수 중 넣을 수 있는 수를 넣는다. 넣을 수 있는 수는
빈 칸의 행, 열, 3*3정사각형에 없는 수임을 확인하자. 확인이 되면 그 빈칸에는
그 수를 넣어준다.

그 다음 빈칸에 대해서도 같은 방법을 수행한다.

마지막 빈칸까지 채우면 스도쿠를 완성하므로 맵을 출력한다.
'''

import sys
graph=[]
blank=[]
for i in range(9):
    graph.append(list(map(int,sys.stdin.readline().rstrip().split())))

for i in range(9):
    for j in range(9):
        if graph[i][j]==0:
            blank.append((i,j))

def checkRow(x,a):
    for i in range(9):
        if a==graph[x][i]:
            return False
    return True
        
def checkCol(y,a):
    for i in range(9):
        if a==graph[i][y]:
            return False
    return True

def checkRect(x,y,a):
    nx=x//3*3
    ny=y//3*3
    for i in range(3):
        for j in range(3):
            if a==graph[nx+i][ny+j]:
                return False
    return True

def dfs(idx):
    if idx==len(blank):
        for i in range(9):
            print(*graph[i])
        exit(0)

    for i in range(1,10):
        x=blank[idx][0]
        y=blank[idx][1]

        if checkRow(x,i) and checkCol(y,i) and checkRect(x,y,i):
            graph[x][y]=i
            dfs(idx+1)
            graph[x][y]=0

dfs(0)