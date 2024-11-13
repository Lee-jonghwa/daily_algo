import sys
sys.stdin = open('18767.txt','r')

# 최고 이동 횟수는 3번
# 무조건 졸이 있는 방향으로 움직여야 함
# 4방향으로 가보면서 졸이 있는지 확인
# 기본적으로 하나를 지나쳐야 이동할 수 있음
# 끝까지 가야하므로 일단 dfs
directions = [(1,0),(-1,0),(0,1),(0,-1)]

def dfs(move, pos):
    # 종료조건 -> 최대 3번 움직임
    if move == 3:
        return

    for dy, dx in directions: # 움직일 수 있는 방향에 대해
        ny, nx = pos[0], pos[1]
        cnt = 0 # dfs를 하기 전 2개 이상을 만나면 break, 0개를 만나도 break
        while True: # 끝까지 갈 때까지 전진
            # 한 칸 전진
            ny += dy
            nx += dx
            # 배열 벗어나면 노
            if ny >= N or ny < 0 or nx >= N or nx < 0: break
            # 한 번 갈 때 연달아 2개 만나면 노
            if cnt >= 2: break
            if cnt == 1: # 이동할 수 있으면
                if arr[ny][nx]: # 값이 있으면
                    visited.add((ny,nx))
                    arr[ny][nx] = 0 # 잡기
                    dfs(move+1, (ny,nx))
                    arr[ny][nx] = 1 # 돌아오기
                else: # 값이 없으면
                    # 전진
                    dfs(move+1, (ny,nx))

            # 1을 만나면
            if arr[ny][nx] == 1:# 갈 수 있으면
                cnt +=1


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    start_pos = (0,0)
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start_pos=(i,j)
                arr[i][j] = 0 # 시작 부분 0 처리
                break
    # 한 번 잡은 걸 다시 잡을 수 없으므로 set 처리
    visited = set()
    dfs(0,start_pos)
    print(f'#{tc} {len(visited)}')




"""
def dfs(s, arr, move):
    global lst
    # 종료조건 => 최고 이동 수
    if move == 3:
        return
    # 현재 위치
    cy, cx = s
    # 4 방향에 대해서
    for dir_y, dir_x in dirs:
        # 다음칸 전진
        ny = cy + dir_y
        nx = cx + dir_x
        # 현재 가는 방향에 대해서 만나는 졸의 개수
        cnt = 0
        # 경계 안이라면
        if 0 <= ny < N and 0 <= nx < N:
            # 졸이면
            if arr[ny][nx] == 1:
                # cnt 증가
                cnt += 1
            # 끝까지 가보기
            while True:
                # 가는 길로 한 칸 전진
                ny += dir_y
                nx += dir_x
                # 만약 만나는 개수가 2개 이상이면(연달아서 2개 만나면)
                if cnt >= 2:
                    break

                #배열 다시 찾기
                if 0 <= ny < N and 0 <= nx < N:
                    # 하나 만난 상태에서 (이동할 수 있는 상태에서)
                    if cnt == 1:
                        # 다음 칸이 졸이면
                        if arr[ny][nx] == 1:
                            # 다음 칸에 방문한 적이 없으면
                            if [ny, nx] not in lst:
                                # 배열 저장
                                lst.append([ny, nx])
                            # 위치 이동
                            arr[ny][nx], arr[cy][cx] = 2, 0
                            # 다음칸에 대한 dfs -> cnt도 초기화 되기때문에 상관 없음
                            dfs([ny, nx], arr, move + 1)
                            # 원래 상태로 복원
                            arr[ny][nx], arr[cy][cx] = 1, 2
                        else: # 다음 칸이 졸이 아니면
                            # 위치 이동
                            arr[ny][nx], arr[cy][cx] = 2, 0
                            # 다음 칸에 대한 dfs
                            dfs([ny, nx], arr, move + 1)
                            # 원상태 복원
                            arr[ny][nx], arr[cy][cx] = 0, 2
                else: # 배열 벗어나면 종료
                    break
                if arr[ny][nx] == 1: # 다음칸이 졸이면
                    cnt += 1 #증가 => while loop 재순회

dirs = (-1, 0), (1, 0), (0, -1), (0, 1)
T = int(input())
for test_case in range(1, 1 + T):
    N = int(input())
    arr_data = [list(map(int, input().split())) for _ in range(N)]
    lst = []
    position = [0, 0]
    # 시작위치 찾기
    for i in range(N):
        for j in range(N):
            if arr_data[i][j] == 2:
                position = [i, j]

    dfs(position, arr_data, 0)
    print(f'#{test_case} {len(lst)}')
"""