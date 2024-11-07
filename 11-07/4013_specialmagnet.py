import sys
sys.stdin = open('4013_input.txt','r')
# K 번 자석을 회전시킨 후 획득하는 점수의 총 합
# 하나의 자석이 1 칸 회전될 때, 서로 붙어 있는 날의 자성과 다를 경우에만 반대 방향으로 1 칸 회전
N=0
S=1
t_right = 1
t_left = -1

def next_turn(now, bef, move_dir,mag_info):

    if move_dir == t_right: # 시계면
        for i in range(8):
            mag_info[bef][i] = mag_info[bef][(i - 1 + 8) % 8] # 지나간 거 이동
        # 모든 날 하나 오른쪽 이동
        if now < 4: # 아직 갈 곳 있으면
            next = now + 1
            next_dir = t_left
            next_turn(next, now, next_dir, mag_info)
    elif move_dir==t_left: # 반시계면
        # 시계로 한 칸씩 이동
        for i in range(8):
            mag_info[mag_num][i] = mag_info[mag_num][(i - 1 + 8) % 8]
            if now < 3: # 아직 갈 곳 있으면
                next = now + 1
                next_dir = t_right
                next_turn(next, now, next_dir, mag_info)
    else: # 왼쪽에 있으면
        # 배열을 벗어나거나 이전 것의 6과 지금 것의 2를 비교
        if now < 0: return
        if mag_info[now][2] == mag_info[bef][6]: # 같으면
            return # 종료
        else: # 다르면
            if move_dir == t_right:  # 시계면
                # 반시계로 한 칸씩 이동
                for i in range(8):
                    mag_info[mag_num][i] = mag_info[mag_num][(i + 1) % 8]
                    if now >= 1 :  # 아직 갈 곳 있으면
                        next = now - 1
                        next_dir = t_left
                        next_turn(next, now, next_dir, mag_info)
            elif move_dir == t_left:  # 반시계면
                # 시계로 한 칸씩 이동
                for i in range(8):
                    mag_info[mag_num][i] = mag_info[mag_num][(i - 1 + 8) % 8]
                    if now >= 1 :  # 아직 갈 곳 있으면
                        next = now - 1
                        next_dir = t_right
                        next_turn(next, now, next_dir, mag_info)
    return
    # if move_dir == t_left: # 시계방향 이동하면
    #     # 모든 날 하나 왼쪽으로 이동
    #     for i in range(8):
    #         new_mag[mag_num][i] = mag_info[mag_num][(i+1)%8]
    #     # 주위의 체인과 비교하기
    #     next_left = mag_num - 1
    #     next_right = mag_num + 1
    #     if next_left >=0:
    #         next_turn(next_left,mag_num,move_dir,new_mag)
    #     elif next_right < 4:
    #         next_turn(next_right,mag_num,move_dir, new_mag)


def turn(now,bef,move_dir,mag_info): # 변경
    if now >= 4 or now <0: return # 배열을 벗어나면 정지
    if now > bef and mag_info[now][6] == mag_info[bef][2]: return # 오른쪽에 있고, 비교했을 때 같으면
    if now < bef and mag_info[now][2] == mag_info[bef][6]: return # 오른쪽에 있고, 비교했을 때 다르면
    if now == bef: # 시작이면
        next_left = mag_num - 1
        next_right = mag_num + 1
        if 4 > next_right >= 0:

        elif 4 > next_left >= 0:
        pass
    elif now > bef: # 오른쪽이면
        if mag_info[now][6] == mag_info[bef][2]: # 같으면
            pass
    elif now < bef: # 왼쪽이면
        if mag_info[now][2] == mag_info[bef][6]: # 같으면
            pass
        move_row = mag_info[mag_num][:] # 현재 이동할 열 저장 및 바꾸기
        if move_dir == t_right:  # 시계면
            # 시계로 한 칸씩 이동
            for i in range(8):
                move_row[i] = mag_info[mag_num][(i - 1 + 8) % 8]
        else:
            # 반시계로 한 칸씩 이동
            for i in range(8):
                move_row[i] = mag_info[mag_num][(i + 1) % 8]
    # 양옆으로 나가기
    next_left = mag_num - 1
    next_right = mag_num + 1
    next_turn(next_left,mag_num,move_dir,mag_info)
    next_turn(next_right,mag_num,move_dir, mag_info)
    return

def score(row):
    if mag_info[row][0] == N:
        return 0
    else:
        return 1*(2**(row))

T = int(input())

# 자석은 총 4개
for tc in range(1,T+1):
    # 회전 횟수
    K = int(input())
    mag_info = [list(map(int,input().split())) for _ in range(4)]
    move_mag = [list(map(int,input().split())) for _ in range(K)]

    '''
    1 번 빨간색 화살표 위치 N 극이면 0 점, S 극이면 1 점을 획득한다.
    2 번 빨간색 화살표 위치 N 극이면 0 점, S 극이면 2 점을 획득한다.
    3 번 빨간색 화살표 위치 N 극이면 0 점, S 극이면 4 점을 획득한다.
    4 번 빨간색 화살표 위치 N 극이면 0 점, S 극이면 8 점을 획득한다
    '''
    # 빨간색 화살표 위치는 항상 0 => 하나 바꾸고 옆에 것 바꾸는 방식으로 가야할 듯
    # 접하는 위치는 체인이 첫번째는 2, 4번째는 6만, 2,4번째는 2,6 자리
    # 이전 체인의 2와 다음 체인의 6을 비교하는 방식
    for mag_num, move_dir in move_mag:
        visited = [0] * 4
        visited[mag_num] = 1
        turn(mag_num-1,mag_num-1,move_dir,mag_info)
    result = 0
    for i in range(4):
        result += score(i)