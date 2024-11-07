from collections import deque
from itertools import combinations
# 유권자의 수 차이가 최소

def is_connected(group, adjArr):
    if not group: # group에 아무것도 없으면
        return False
    else: # 그룹이 있으면
        visited = [0] * N
        q = deque()
        # 어쨌든 다 연결돼야 하니까 하나부터 시작해서 연결시키면 됨
        q.append(group[0])
        visited[group[0]] = 1
        while q:
            w = q.popleft()
            for v in range(N): # 인접한 아이들에 대해 순회
                if adjArr[w][v]==1 and v in group and visited[v]==0:
                    visited[v] = 1
                    q.append(v)
        return len(group) == sum(visited)

# 마을의 수
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    villages = list(range(N))
    adjArr = [list(map(int, input().split())) for _ in range(N)]
    # 마을별 유권자수
    P = list(map(int, input().split()))
    # bfs-> dfs
    min_v = float('inf')
    for n in range(1, N // 2 + 1):
        # 중복을 허용하는 순서대로 a를 넣기(1~n개)
        for group_a in combinations(villages,n):
            # b는 그 나머지
            group_b = [v for v in villages if v not in group_a]
            # 두 그룹의 연결을 확인하기
            if is_connected(group_a, adjArr) and is_connected(group_b, adjArr):
                # 다 연결됐으면 합산
                voters_a = sum(P[v] for v in group_a)
                voters_b = sum(P[v] for v in group_b)
                voters_diff = abs(voters_b - voters_a)
                min_v = min(min_v,voters_diff)
    print(f'#{tc} {min_v}')