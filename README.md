# 10월 21일
### 체스판 다시 칠하기
```python

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
```


# 10월 18일
### 미로 탐색
```python
from collections import deque

def bfs(s_y, s_x, e_y, e_x):
    q = deque()
    q.append((s_y,s_x))
    visited[s_y][s_x] = 1
    while q:
        now_y, now_x = q.popleft()
        if now_y == e_y and now_x == e_x:
            return visited[e_y][e_x]

        for dy, dx in directions:
            ny, nx = now_y+dy, now_x+dx
            if 0 <= ny < N and 0 <= nx < M:
                if visited[ny][nx] == 0 and arr[ny][nx] == 1:
                    q.append((ny,nx))
                    visited[ny][nx] = visited[now_y][now_x] + 1
    return -1

N, M = map(int,input().split())

arr = [list(map(int,input())) for _ in range(N)]
directions = [(0,1),(0,-1),(1,0),(-1,0)]

start = (0, 0)
end = (N-1, M-1)
visited = [[0] * M for _ in range(N)]

result = bfs(start[0], start[1], end[0], end[1])

print(result)
```

# 10월 17일

### DFS와 BFS
```python
"""
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
"""

N, M, V = map(int,input().split())
"""
N: 정점 개수
M: 간선 개수
V: 시작점
"""

def dfs(c):
    for w in adjL[c]: # 인접한 곳에 대해서
        if visited[w] == 0:
            result_dfs.append(w) # path 추가
            visited[w] = 1 # 방문표시
            dfs(w) # 돌아올 필요 없이 다 방문만 하면 됨

def bfs(s):
    q = []
    q.append(s)
    visited[s] = 1
    result_bfs.append(s)

    while q:
        s = q.pop(0) # 현재 위치 반환
        for w in adjL[s]: # 접점이 있는 곳에서
            if visited[w] == 0: # 안 간 곳
                visited[w] = 1 # 방문
                q.append(w) # 인큐
                result_bfs.append(w)


adjL = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adjL[a].append(b)
    adjL[b].append(a)

for i in range(1, N+1): # 순서대로 방문하기 위해서 오름차순 정렬
    adjL[i].sort()


visited = [0]*(N+1)
result_dfs = [V]
visited[V] = 1
dfs(V)

visited = [0]*(N+1)
result_bfs = []
bfs(V)

print(*result_dfs)
print(*result_bfs)
```


### 단지 번호 붙이기
```python
# 순회하면서 0이 아닌 곳을 만나면 bfs
# bfs 인큐 시 cnt 증가
# 방문표시를 추가해서 경우 줄이기

def bfs(s_y,s_x):
    q = []
    q.append((s_y,s_x))
    visited[s_y][s_x] = 1 # 방문 표시
    cnt = 1 # 시작자리 포함
    while q:
        now = q.pop(0)
        for dy, dx in directions:
            ny, nx = now[0]+dy, now[1]+dx
            # 배열 벗어나지 않고, 방문한 적 없으며, 1인 경우
            if 0 <= ny < N and 0 <= nx <N and visited[ny][nx] == 0 and arr[ny][nx] == 1:
                q.append((ny,nx))
                visited[ny][nx] = 1
                cnt += 1
    return cnt

directions = [(0,1),(0,-1),(1,0),(-1,0)]
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]


visited = [[0] * N for _ in range(N)]

num_count = [] # 결과 배열

for i in range(N):
    for j in range(N):
         # 방문표시
        if visited[i][j] == 0 and arr[i][j] == 1: # 0이 아닌 곳이 발견되면
            #bfs시작
            num_count.append(bfs(i,j))
        visited[i][j] = 1

num_count.sort()
print(len(num_count))
for z in range(len(num_count)):
    print(num_count[z])
```

# 10월 16일

### N과 M(2)

```python
# 조합 문제이므로 중복이 없어야 함 -> 시작점을 점점 좁히기
def dfs(lev, start):
    if lev == M:
        print(*path)
        return
    for i in range(start, len(numbers)):
        path.append(numbers[i]) # path 기록
        dfs(lev + 1, i + 1) # 레벨 증가
        path.pop()

# N: branch
# M: lev
N, M = map(int, input().split())

numbers = [i for i in range(1, N+1)]

path = [] # 경로 저장

dfs(0,0) # dfs 진행

```

### N과 M(4)

```python
#N: branch
#M: lev
N, M = map(int, input().split())

numbers = [i for i in range(1, N+1)]

path = [] # 경로 저장

# 중복이 가능한 조합이므로 visited 필요 없음, start 좁히기 필요
def dfs(lev, start):
    if lev == M:
        print(*path)
        return

    for j in range(start, N+1):
        path.append(j)
        dfs(lev+1, j) # 현재 있는 수도 포함하여 다음 진행
        path.pop()

dfs(0,1)
```

### N과 M(5)

```python
N, M = map(int, input().split())
# N: branch
# M: lev
numbers = list(map(int, input().split()))
numbers.sort() # 오름차순 정리

path = [] # 경로 저장
visited = [0] * N # 방문표시

def dfs(lev): # 중복 순열 -> 중복 허용하므로 일반적인 스타일의 visited 필요
    if lev == M:
        print(*path)
        return

    for i in range(N):
        if visited[i] == 0: # 방문하지 않은 곳에 대해
            path.append(numbers[i])
            visited[i] = 1
            dfs(lev+1)
            visited[i] = 0
            path.pop()


dfs(0)
```

### 헌내기는 친구가 필요해

```python
from collections import deque

def finding_start(arr): # 시작점 찾기
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'I': # 찾으면
                return (i,j) # 바로 정지

def bfs(start): # 시작점부터 순회
    queue = deque()
    queue.append(start) # 시작점 등록
    visited[start[0]][start[1]] = 1 # 방문표시
    count = 0

    while queue:
        now_y, now_x = queue.popleft()
        for dy, dx in directions: # 가능한 방향에서
            next_y, next_x = now_y + dy, now_x + dx # 다음 지정하기
            if 0 <= next_y <N and 0 <= next_x < M: # 배열을 벗어나지 않는 선에서
                if visited[next_y][next_x] == 0 and arr[next_y][next_x] != 'X': # 방문한 적이 없고, 벽이 아니면
                    queue.append((next_y, next_x)) # 인큐
                    visited[next_y][next_x] = 1 # 방문표시
                    if arr[next_y][next_x] == 'P': # 사람만나면 증가
                        count += 1

    # 특정 종료 조건이 없으므로 순회하게 놔두기
    if count > 0: # 사람 만났으면
        return count # 사람 수 반환
    else: # 못 만났으면
        return 'TT' # 울기



directions = [(0,1),(0,-1),(-1,0),(1,0)]
# 맵의 세로 가로
N, M = map(int,input().split())

arr = [input() for _ in range(N)] # 맵 생성

start = finding_start(arr) # 시작점 찾기
visited = [[0]*M for _ in range(N)] # visitied 배열 생성

result = bfs(start) #결과 저장
print(result)
```