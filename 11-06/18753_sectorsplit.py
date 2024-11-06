from collections import deque
from itertools import combinations
# 유권자의 수 차이가 최소

def find_min(s): # s: 시작 노드
    visited = [0]*4
    q=deque()
    q.append(s)
    visited[s] = 0
    sec_A = [] # A 지역구
    while q:
        w = q.popleft()


# 마을의 수
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    villages = list(range(N))
    adjArr = [list(map(int, input().split())) for _ in range(N)]
    # 마을별 유권자수
    P = list(map(int, input().split()))
    print(adjArr)
    # bfs-> dfs
    min_v = 160
    for n in range(4):
        for group_a in combinations(villages,n):
            group_b = [v for v in villages if v not in group_a]

            if is_connected(group_a, adjArr) and is_connected(group_b, adjArr):
                voters_a = sum(v)
        result = find_min(n)
        min_v = min(min_v,result)
    print(f'#{tc} {min_v}')