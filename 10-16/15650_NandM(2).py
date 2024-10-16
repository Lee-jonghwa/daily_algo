# 조합 문제이므로 중복이 없어야 함 -> 시작점을 점점 좁히기
def dfs(lev, start):
    if lev == M:
        print(*path)
        return
    for i in range(start, len(numbers)):
        path.append(numbers[i]) # path 기록
        dfs(lev + 1, i + 1) # 레벨 증가
        path.pop()

# N: branch
# M: lev
N, M = map(int, input().split())

numbers = [i for i in range(1, N+1)]

path = [] # 경로 저장

dfs(0,0) # dfs 진행
