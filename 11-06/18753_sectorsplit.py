from itertools import combinations
from collections import deque


def sum_town(town):
    sum_v = 0
    for i in town:
        sum_v += P[i]
    return sum_v

# 그룹이 내부에서 서로 연결된 걸 알아보기 위함
# 인접행렬과 비교하면서 값이 있으면 연결 표시, 하나라도 안 되어 있으면 탈락
def is_connected(town, arr):
    if not town: return False# 아무것도 담겨져 있지 않으면 패스

    # 마을 방문 배열 생성
    visited = [0] * N
    # 널리 퍼져서 최대한 연결된 걸 빨리 찾아야 하므로 bfs
    q = deque()
    q.append(town[0])
    while q:
        now = q.popleft()
        visited[now] = 1 # 방문처리

        for j in range(N): #모든 후보에 대해서
            # 인접하고, 그룹안에 있고 town에 있으면
            if arr[now][j] ==1 and j in town and visited[j] == 0:
                q.append(j)
    # 방문한 배열과 town의 길이가 같으면 통과
    return len(town) == sum(visited)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 마을 번호 => 유권자 수 잘 뽑기 위해서 P 인덱스에 맞춤
    towns = [_ for _ in range(N)]
    arr = [list(map(int,input().split())) for _ in range(N)]
    P = list(map(int,input().split()))

    min_v = float('inf')
    # 마을 2개로 나누는 건 나눠서 구하는 하나의 절차를 끝까지 가야함
    # 마을을 나누는 건 조합을 활용 => 안에서 연결짓는 건 bfs
    for i in range(1, N//2+1):
        # 2개로 나누는 모든 조합 구함,
        # 적어도 1개는 있어야 하며, N//2개 이상이 되면 동일하므로 절반 수행
        for town_a in combinations(towns,i):
            # b 는 towns에서 a에 들어있지 않은 곳으로
            town_b = [town for town in towns if town not in town_a]
            # 각각의 마을들이 서로 연결되어 있으면
            if is_connected(town_a,arr) and is_connected(town_b,arr):
                sum_a = sum_town(town_a)
                sum_b = sum_town(town_b)
                diff_ab = abs(sum_a-sum_b)
                min_v = min(min_v,diff_ab)

    print(f'#{tc} {min_v}')



"""

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

"""