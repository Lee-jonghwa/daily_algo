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

def dfs(V):
    s = V

    for w in adjL[s]:
        if visited[w] == 1: continue
        path1.append(w)
        visited[w] = 1
        dfs(w)
        visited[w] = 0
        path1.pop()

    return path1


def bfs(V):
    q = []
    q.append(V)
    visited[V] = 1
    path = [V]

    while q:
        s = q.pop(0)

        for w in adjL[s]:
            if visited[w] == 0:
                visited[w] = 1
                q.append(w)
                path.append(w)

    return path

adjL = [[] for _ in range(N+1)]
Lines = [list(map(int, input().split())) for _ in range(M)]

for i in range(M):
    a = Lines[i][0]
    b = Lines[i][1]
    adjL[a].append(b)
    adjL[b].append(a)

print(adjL)

visited = [0]*(N+1)
visited[V] = 1
path1 = [V]
path1 = dfs(V)

visited = [0]*(N+1)
path2 = bfs(V)

print(*path1)
print(*path2)