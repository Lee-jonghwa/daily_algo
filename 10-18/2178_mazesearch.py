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