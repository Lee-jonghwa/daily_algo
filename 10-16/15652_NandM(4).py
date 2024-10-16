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