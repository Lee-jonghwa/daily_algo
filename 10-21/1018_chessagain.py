
# 완전탐색으로 접근해보기

N, M = map(int,input().split())
arr = [list(input()) for _ in range(N)]

# 매 행을 순회하면서 패턴을 비교함, 불일치하면 다시 보기
pat1 = 'WBWBWBWBWB'
pat2 = 'BWBWBWBWBW'

ans1 = [pat1, pat2, pat1, pat2, pat1, pat2, pat1, pat2]
ans2 = [pat2, pat1, pat2, pat1, pat2, pat1, pat2, pat1]

min_num = N*M # 다 바꾸는 게 최대 횟수

# 각각의 위치에서 패턴 비교
for i in range(N-7): # 횟수 줄이기-> 8*8까지만 비교하면 됨
    for j in range(M-7):
        cnt1 = 0
        cnt2 = 0
        for di in range(8):
            for dj in range(8):
                if arr[i+di][j+dj] != ans1[di][dj]:
                    cnt1 += 1
        for di in range(8):
            for dj in range(8):
                if arr[i+di][j+dj] != ans2[di][dj]:
                    cnt2 += 1
        min_num = min(cnt1,cnt2,min_num)

print(min_num)


""" bfs는 실패,,, 다시 조건 생각해보기
from collections import deque

def bfs(sy,sx, ey, ex):
    q = deque()
    q.append((sy,sx))
    visited = [[0]*M for _ in range(N)] #여기선 의미없음
    visited[sy][sx] = 1
    cnt = 0
    while q:
        cy, cx = q.popleft()
        if cnt >= min_num: # 가지치기
            return cnt

        for dy, dx in directions:
            ny, nx = cy + dy, cx + dx
            if sy <= ny <= ey and sx <= nx <= ex and visited[ny][nx] == 0:
                if color_arr[cy][cx] == 'B' and color_arr[ny][nx] == 'B': # 지금과 다음은 무조건 달라야하므로 수정
                    cnt += 1
                    color_arr[ny][nx] = 'W'
                elif color_arr[cy][cx] == 'W' and color_arr[ny][nx] == 'W':  # 지금과 다음은 무조건 달라야하므로 수정
                    cnt += 1
                    color_arr[ny][nx] = 'B'
    return cnt

N, M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
color_arr = arr # 색칠한 것 반영하는 배열 생성
directions = [(0,1),(1,0)] # 좌측 위부터 시작하기 때문에 우측, 아래만 가면 될 것 같음


min_num = N*M # 다 바꾸는 게 최대 횟수

# 각각의 위치에서 bfs 진행, 종료점을 시작점 +7 로 하면 매 번 bfs 확인할 수 있음
for i in range(N-7): # 횟수 줄이기
    for j in range(M-7):
        num = bfs(i,j,i+7,j+7)
        if min_num > num:
            min_num = num

print(min_num)

"""