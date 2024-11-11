import sys
sys.stdin = open('2105_input.txt','r')

directions = [(1,1),(1,-1),(-1,-1),(-1,1),(1,1)]

# 같은 방향으로 가면 w_c 증가, 아니면 h_c 증가 => 걍 방향만 봐도 될듯??
# 한 사각형에 속하면 경우는 다 같다. 즉 밑에 경우에 크게 신경쓰지 않아도 됨
# 우측 하단, 좌측 하단만 보고, 반대는 -로 돌아오면 될 듯 -> - 씌우는 게 종료조건이 너무 어려움 그냥 모든 방향 하기
def dfs(y, x, now_dir, path, s_pos):
    global max_v

    # 종료조건(성공)
    if now_dir == 3 and y==s_pos[0] and x==s_pos[1]: # 돌아오는 길에 시작점 만나면
        max_v = max(len(path), max_v) # 이미 다음 거 보내기 전에 path에 넣으므로 여기선 따로 path를 건드릴 필요는 없음
        return

    # 종료조건(실패)
    if now_dir > 3: # 한바퀴 이상 돌면
        return


    for next_dir in (now_dir, now_dir+1): # 전진하거나 꺾는 거 중 하나
        dy, dx = directions[next_dir]
        ny, nx = y + dy , x + dx
        # 배열을 벗어나지 않고 방문하지 않은 곳, 중복값이 없으면
        if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] not in path:
            # 갈 곳이 정해졌으면
            path.append(arr[ny][nx])
            dfs(ny, nx, next_dir, path,s_pos)
            path.pop()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    # 맵을 순회
    # 각 자리마다 갈 길을 탐색
    # path, visited 생성 -> 매 건마다
    # 최장 경로니까 DFS해볼까?
    # 사각형을 그려야함 -> 갔던 만큼 대칭적으로 돌아와야함, 지그재그 범위X
    # dfs랑은 의미가 다른 것 같지만,,, 일단 고
    max_v = -1
    # y축은 시작점 밑에 두 칸은 있어야 함
    for i in range(N-2):
        # x 축은 시작점 양옆에 한 칸은 있어야 함
        for j in range(1,N-1):
            dfs(i,j, 0, [], (i,j))
    print(f'#{tc} {max_v}')