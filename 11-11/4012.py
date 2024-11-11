import sys
sys.stdin = open('4012.txt', 'r')

def dfs(lv, alst, blst):
    global min_v
    if lv == N:  # 2/N개를 뽑으면
        if len(alst)== (N//2):
            sum_a = 0
            sum_b = 0
            for i in range(N//2):
                for j in range(i+1, N//2):  # i랑 j는 겹치지 않게
                    sum_a += arr[alst[i]][alst[j]]
                    sum_a += arr[alst[j]][alst[i]]
                    sum_b += arr[blst[i]][blst[j]]
                    sum_b += arr[blst[j]][blst[i]]
            result = abs(sum_b - sum_a)
            min_v = min(result, min_v)
        return

    dfs(lv+1, alst+[lv], blst) # 현재 위치를 alst에 추가
    dfs(lv+1, alst, blst+[lv]) # 현재 위치를 blst에 추가


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    Nlst = [_ for _ in range(N)]
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    min_v = 20000 * N * N
    # dfs로 경우의 수 나누기

    dfs(0, [], [])

    print(f'#{tc} {min_v}')

"""
## 시간 초과,,,,, 다른 방법으로 해봐야할 듯
def dfs(lv, alst, visited):
    global min_v
    if lv == (N//2): # 2/N개를 뽑으면
        blst = [v for v in Nlst if v not in alst]
        sum_a = 0
        sum_b = 0
        for i in range(len(alst)):
            for j in range(i + 1, len(alst)):  # i랑 j는 겹치지 않게
                sum_a += arr[alst[i]][alst[j]]
                sum_a += arr[alst[j]][alst[i]]
                sum_b += arr[blst[i]][blst[j]]
                sum_b += arr[blst[j]][blst[i]]
        result = abs(sum_b - sum_a)
        min_v = min(result, min_v)
        return

    for n in range(N): # 모든 후보군에 대해
        if not visited[n]: # 방문 안 하면
            visited[n] = 1
            alst.append(n)
            dfs(lv+1, alst, visited)
            alst.pop()
            visited[n] = 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    Nlst = [_ for _ in range(N)]
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0]*N
    min_v = 20000*N*N
    # dfs로 경우의 수 나누기

    alst = []
    dfs(0, alst, visited)

    print(f'#{tc} {min_v}')
"""