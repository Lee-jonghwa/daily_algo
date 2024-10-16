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