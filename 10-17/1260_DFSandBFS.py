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