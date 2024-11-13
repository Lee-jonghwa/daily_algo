import sys
sys.stdin = open('18567.txt','r')

def robot(y, x, dir):
    global ans
    cy, cx, cdir = y, x, dir
    # 수확 현황을 위한 테이블
    seed_arr = [[0] * N for _ in range(N)]
    # 일 수 계산을 위한 테이블
    area = [i[:] for i in arr]
    cnt = 0
    # 일수 동안에
    for time in range(M):
        # backtraking
        # 남은 기간이 움직일 수 있는 횟수보다 적으면 정지 => 가지치기
        if M - time < ans - cnt:
            return
        # current_area define
        # 기본은 수확할 수 없는 상태
        can_harvest = False
        # 수확할 수 있는 맵에 대해 만약 0이 아니고, 날짜보다 작으면
        if area[cy][cx] != 0 and area[cy][cx] <= time:
            # 수확할 수 있는 상태
            can_harvest = True
        # move define
        # 기본은 움직일 수 없는 상태
        can_move = False
        next_data = []
        # 현재 방향을 기준으로 다음으로 가는 방향들 모두 평가
        for diry, dirx, ndir in dirs_dict[cdir]:
            ny = cy + diry
            nx = cx + dirx
            # 배열을 벗어나지 않고, 산이 아니면서, 곡물을 수확할 수 있거나, 0인 값에 대해서
            if 0 <= ny < N and 0 <= nx < N and area[ny][nx] != 1 and (area[ny][nx] == 0 or area[ny][nx] <= time):
                # 움직일 수 있는 상태
                can_move = True
                # 다음 위치 저장
                next_data = [ny, nx, ndir]
                break # 찾았으니 중지
        # 지가간 자리 처리
        # 현재 농지가 빈 농지이고 로봇이 다음 농지로 이동할 수 있으면
        if area[cy][cx] == 0 and can_move:
            # 씨를 심음 -> +=1 은 k번째 처리
            seed_arr[cy][cx] += 1
            # area update
            # 그 자리에서 수확할 수 있는 시간을 정함
            # 수확할 수 있는 농지에 씨를 심은 시기 + 자라는 시간 + 날짜
            area[cy][cx] = seed_arr[cy][cx] + 4 + time
        # 현재가 빈 농지고 아무것도 못하면
        elif area[cy][cx] == 0 and not can_move:
            # 아무 행동 안함
            pass
        # 수확할 수 있으면
        elif can_harvest:
            # 빈농지
            area[cy][cx] = 0
            # 수확
            cnt += 1

        if can_move:
            cy, cx, cdir = next_data
        else:
            continue
    ans = max(ans, cnt)


T = int(input())
for test_case in range(1, 1 + T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    dirs_dict = {
        # 현재 바라보는 방향 : 이동하는 방향 및 바라보게 될 방향
        # 이동 순서가 바라보는 방향 기준 오 앞 왼 뒤 순서
        0: ((1, 0, 1), (0, 1, 0), (-1, 0, 3), (0, -1, 2)),
        1: ((0, -1, 2), (1, 0, 1), (0, 1, 0), (-1, 0, 3)),
        2: ((-1, 0, 3), (0, -1, 2), (1, 0, 1), (0, 1, 0)),
        3: ((0, 1, 0), (-1, 0, 3), (0, -1, 2), (1, 0, 1))
    }
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 1:
                # 1이 아닌 모든 곳에 대해 평가
                for k in range(4):
                    # k -> 바라보는 방향
                    robot(i, j, k)
    print(f'#{test_case} {ans}')
