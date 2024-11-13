import sys
sys.stdin = open('22755.txt','r')

from itertools import permutations
from copy import deepcopy

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(N)]
    rcs = [list(map(int, input().split())) for _ in range(K)]

    ans = 987654321

    # 1. 회전 순서 정하기 (최대 6!=720)
    for p in permutations(rcs, K): # 리스트에서 K개를 뽑는 경우의 수 리스트에서
        # p 라는 요소(rcs의 모음)을 추출함
        # 만약 permutations 안 되면 dfs로 해야지 머
        # 2. 회전
        # copy_a = [row[:] for row in a] 밑이랑 같은 표현
        copy_a = deepcopy(a)  # 원본리스트 카피
        for r, c, s in p:
            r -= 1
            c -= 1
            for n in range(s, 0, -1): # 범위 줄이기, 겉 부터 안으로(순서 상관 없을 듯)
                tmp = copy_a[r-n][c+n] # 우측 상단 뽑기
                # 왼쪽부터 2n개를 오른쪽으로 한 칸 옮김 -> 배열을 벗어날 일 없음
                copy_a[r-n][c-n+1:c+n+1] = copy_a[r-n][c-n:c+n]
                # 왼쪽 끝행을 가장 밑에 부터 2n개를 하나씩 올림
                for row in range(r-n, r+n):
                    copy_a[row][c-n] = copy_a[row+1][c-n]
                # 오른쪽부터 2n개를 왼쪽으로 한 칸 옮김
                copy_a[r+n][c-n:c+n] = copy_a[r+n][c-n+1:c+n+1]  # 오른쪽 걸 왼쪽으로 바꿈
                # 오른쪽 끝행을 가장 위부터 2n개를 하나씩 내림
                for row in range(r+n, r-n, -1):  # 오른쪽 위에 걸 밑으로 바꿈
                    copy_a[row][c+n] = copy_a[row-1][c+n]
                # 하나는 바뀌어졌던 게 밀려내려오므로 tmp로 저장했던 것 끼우기
                copy_a[r-n+1][c+n] = tmp # 우측 상단 끼우기

        # 3. 각 행의 최소값 찾기
        for row in copy_a:
            ans = min(ans, sum(row))

    print(f'#{tc} {ans}')
