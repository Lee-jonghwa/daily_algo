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

Lines = [list(map(int, input().split())) for _ in range(M)]

print(Lines)