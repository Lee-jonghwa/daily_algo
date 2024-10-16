N, M = map(int, input().split())
# N: branch
# M: lev
numbers = list(map(int, input().split()))
numbers.sort() # 오름차순 정리

path = [] # 경로 저장
visited = [0] * N # 방문표시

def dfs(lev): # 중복 순열 -> 중복 허용하므로 일반적인 스타일의 visited 필요
    if lev == M:
        print(*path)
        return

    for i in range(N):
        if visited[i] == 0: # 방문하지 않은 곳에 대해
            path.append(numbers[i])
            visited[i] = 1
            dfs(lev+1)
            visited[i] = 0
            path.pop()


dfs(0)