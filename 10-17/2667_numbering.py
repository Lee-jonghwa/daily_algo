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