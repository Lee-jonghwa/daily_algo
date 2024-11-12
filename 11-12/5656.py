import sys
sys.stdin = open('5656.txt', 'r')

directions = [(1,0),(-1,0),(0,1),(0,-1)]

def dfs(lev, remains, now_arr):
    global min_v
    if lev == N or remains==0: # N번 다 쏘면
        min_v = min(remains,min_v)
        return

    for col in range(W): # 모든 열에 대해서
        copy_arr = [row[:] for row in now_arr]
        row = -1  # 가장 먼저 만날 높이, 기본적으로 없다고 세팅
        for r in range(H): # 모든 행에 대해서
            if copy_arr[r][col]:
                row = r # 높이 있는 곳 지정
                break # 찾고 빠져나오기
        if row == -1: continue # 없으면 넘김

        # 벽돌 깨기(깨뜨릴 위치와 파워)
        stack = [(row, col, copy_arr[row][col])] # 깰 벽돌 리스트
        now_remains = remains - 1 # 지금까지 깬 벽돌
        copy_arr[row][col] = 0 #시작점 터뜨리기

        while stack:
            y, x, p = stack.pop()
            for k in range(1,p): # 파워만큼 옆으로
                for dy, dx in directions: # 상하좌우
                    ny = y + (dy * k)
                    nx = x + (dx * k)
                    # 배열을 벗어나지 않고
                    if ny < 0 or ny >= H or nx < 0 or nx >= W: continue
                    # 값이 있으면
                    if copy_arr[ny][nx] == 0 : continue

                    stack.append((ny, nx, copy_arr[ny][nx])) # 스택 넣기
                    copy_arr[ny][nx] = 0# 깨뜨리기
                    now_remains -= 1# 남은 갯수 감소

        # 파워 범위만큼 깬 후, 칸을 내려주는 것이 필요
        for c in range(W): # 열 순회 우선(열 내에서 바꾸기 때문)
            idx = H - 1 # 바꿀 자리 가장 밑부터 하나씩 바꿔 올라옴
            for r in range(H-1, -1, -1): # 끝에서부터 올라옴, 모든 행에 대해서 다 순회하게 됨
                if copy_arr[r][c]: # 값이 있으면
                    # 자리 바꾸기
                    copy_arr[r][c], copy_arr[idx][c] = copy_arr[idx][c], copy_arr[r][c]
                    idx -= 1 # 한 칸 올리기
        dfs(lev+1,now_remains,copy_arr)

T = int(input())
for tc in range(1,T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(H)]

    # N 개의 벽돌을 떨어트려 최대한 많은 벽돌을 제거

    # 떨어지는 경우의 수는 모든 행 순회 하는 dfs
    # 만나는 곳이 블록이 없으면 떨어뜨릴 필요 없음
    # 만나는 곳이 있으면 가장 위

    # 깨질 곳 후보 저장 => 확인 후 맵을 다 0으로 바꿈

    # 순회하면서 한 칸씩 아래로 내림

    bricks = 0 # 총 개수 구하기
    for i in range(H):
        for j in range(W):
            if arr[i][j]:
                bricks+=1

    min_v = float('inf')
    dfs(0,bricks, arr)

    print(f'#{tc} {min_v}')