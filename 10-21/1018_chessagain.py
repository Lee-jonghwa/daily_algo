"""
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
"""
"""
from collections import deque

def bfs(sy,sx, ey, ex):
    q = deque()
    q.append((sy,sx))
    visited = [[0]*M for _ in range(N)] #여기선 의미없음
    visited[sy][sx] = 1
    cnt = 0
    color_arr = [arr[i][:] for i in range(N)]  # 색칠한 것 반영하는 배열 생성
    while q:
        cy, cx = q.popleft()
        if cnt >= min_num: # 가지치기
            return cnt

        for dy, dx in directions:
            ny, nx = cy + dy, cx + dx
            if sy <= ny <= ey and sx <= nx <= ex and visited[ny][nx] == 0:
                visited[ny][nx] = 1 # 의미 x
                q.append((ny,nx))
                if color_arr[cy][cx] == 'B' and color_arr[ny][nx] == 'B': # 지금과 다음은 무조건 달라야하므로 수정
                    cnt += 1
                    color_arr[ny][nx] = 'W'
                elif color_arr[cy][cx] == 'W' and color_arr[ny][nx] == 'W':  # 지금과 다음은 무조건 달라야하므로 수정
                    cnt += 1
                    color_arr[ny][nx] = 'B'
    return cnt

N, M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
directions = [(0,1),(1,0)] # 좌측 위부터 시작하기 때문에 우측, 아래만 가면 될 것 같음


min_num = N*M # 다 바꾸는 게 최대 횟수라고 생각

# 각각의 위치에서 bfs 진행, 종료점을 시작점 +7 로 하면 매 번 bfs 확인할 수 있음
for i in range(N-7): # 횟수 줄이기
    for j in range(M-7):
        num = bfs(i,j,i+7,j+7)
        min_num = min(min_num, num)

print(min_num)
"""

## 수정했지만 시간 초과 -> bfs는 안 될 것 같음ㅎㅅㅎ
from collections import deque


def bfs(sy, sx, ey, ex, first_color):
    q = deque()
    q.append((sy, sx))
    cnt = 0
    color_arr = [arr[i][:] for i in range(N)]  # 색칠한 것 반영하는 배열 생성

    while q:
        cy, cx = q.popleft()
        if cnt >= min_num: # 가지치기
            return cnt

        # 첫 번째 칸이 'B'인 경우와 'W'인 경우에 따라 예상 색상을 결정
        expected_color = 'B' if (cy + cx) % 2 == 0 else 'W'
        if first_color == 'W':
            expected_color = 'W' if (cy + cx) % 2 == 0 else 'B'

        # 현재 색상이 예상 색상과 다르면 변환
        if color_arr[cy][cx] != expected_color:
            cnt += 1
            color_arr[cy][cx] = expected_color  # 변환된 색상 적용

        # 다음 이동할 좌표 추가 (오른쪽과 아래쪽만)
        for dy, dx in directions:
            ny, nx = cy + dy, cx + dx
            if sy <= ny <= ey and sx <= nx <= ex:
                q.append((ny, nx))

    return cnt


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
directions = [(0, 1), (1, 0)]  # 오른쪽, 아래 방향으로만 탐색

min_num = N * M  # 다 바꾸는 것이 최대 횟수라고 가정

# 각각의 위치에서 BFS 진행, 종료점을 시작점 + 7로 하면 매번 BFS로 확인할 수 있음
for i in range(N - 7):
    for j in range(M - 7):
        # 두 가지 경우를 비교하여 최소값을 선택
        num1 = bfs(i, j, i + 7, j + 7, 'B')  # 왼쪽 위가 'B'인 경우
        num2 = bfs(i, j, i + 7, j + 7, 'W')  # 왼쪽 위가 'W'인 경우
        min_num = min(min_num, num1, num2)

print(min_num)
