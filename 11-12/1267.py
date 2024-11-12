import sys
sys.stdin = open('1267.txt','r')

from collections import deque

# 위상 정렬 함수
def topology_sort():
    result = []  # 결과 리스트
    q = deque()  # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, V + 1): # 전체를 순회하면서
        if indegree[i] == 0: # 진입차수가 0(이전 조건이 없는 함수)
            q.append(i) # 큐 삽입

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now) # 결과에 삽입

        for i in adjL[now]:  # 갈 수 있는 노드들에 대해서
            indegree[i] -= 1 # 진입 차수 1 줄이기
            if indegree[i] == 0: # 새로운 곳 찾아서
                q.append(i) # 인큐

    # 위상 정렬을 수행한 결과 출력
    return result

T = int(10)
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjs = list(map(int, input().split()))

    adjL = [[] for _ in range(V+1)]
    indegree = [0]*(V+1) # 진입 차수

    for i in range(len(adjs)//2):
        adjL[adjs[2*i]].append(adjs[2*i+1])
        indegree[adjs[2*i+1]]+=1

    result = topology_sort()

    print(f'#{tc}', *result)




