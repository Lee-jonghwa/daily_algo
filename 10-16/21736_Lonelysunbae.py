from collections import deque

def finding_start(arr):
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'I':
                return (i,j)

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