import sys
sys.stdin = open('4013_input.txt','r')

# 문제 이해를 잘못함... 연계돼서 톱니가 도는 게 아닌, 한 지점에서 모든 점이 돌아가는 것임 좀 더 쉽게 풀 수 있었을텐데,,,
"""
# K 번 자석을 회전시킨 후 획득하는 점수의 총 합
# 하나의 자석이 1 칸 회전될 때, 서로 붙어 있는 날의 자성과 다를 경우에만 반대 방향으로 1 칸 회전
N=0
S=1
t_right = 1
t_left = -1


def turn(now,bef,move_dir,mag_info, visited): # 변경
    if now < 0 or now >= len(mag_info) or bef < 0 or bef >= len(mag_info) or visited[now]: return # 배열을 벗어나면 정지

    # 현재위치 반환
    visited[now] = 1
    # 각 방향에 대해 같은 경우 -> 변경 필요 없음
    if (now > bef and mag_info[now][6] == mag_info[bef][2])\
            or (now < bef and mag_info[now][2] == mag_info[bef][6]): return

    next_right = now + 1
    next_left = now - 1


    # 변경
    move_row = mag_info[now][:]  # 현재 이동할 열 저장

    is_go_right = False
    is_go_left = False
    # 다음을 변경할 지 말지를 확인해야 함
    if now>=1 and mag_info[now][6] != mag_info[now-1][2]:
        is_go_left = True
    elif now<3 and mag_info[now][2] != mag_info[now+1][6]:
        is_go_right = True


    if move_dir == t_right:
        move_row = [move_row[(i-1+8) % 8] for i in range(8)]
    else:
        move_row = [move_row[(i+1) % 8] for i in range(8)]
    mag_info[now] = move_row # 바꿔끼우기

    # 양옆으로 가기
    if is_go_left:
        turn(now-1, mag_num, move_dir, mag_info, visited)
    elif is_go_right:
        turn(now+1, mag_num, move_dir, mag_info, visited)
    return

def score(mag_info):
    result = 0
    for i in range(4):
        if mag_info[i][0] == S:
            result += 1 * (2 ** i)
    return result

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
        # 처음은 같음으로 해서 연결
        turn(mag_num-1,mag_num-1,move_dir,mag_info, visited)

    result = score(mag_info)
    print(f'#{tc} {result}')
    
    """

# 옥토푸수 박사님 풀이
T = int(input())
N = 4 # 자석 개수

# 자석은 총 4개
for tc in range(1,T+1):
    # 회전 횟수
    K = int(input())
    arr = [[0]*8] + [list(map(int, input().split())) for _ in range(N)]
    top = [0] * (N+1)
    for _ in range(K): # K번 idx, dr 입력받음(회전)
        idx, dr = map(int, input().split())
        # [1] idx 톱니를 회전
        tlst = [(idx, 0)]
        # [2] 우측방향 처리(같은 극성 나오면 탈출)
        for i in range(idx+1,N+1):
            # 왼쪽 3시 극성 != 오른쪽 9시 극성 -> 회전 후보 추가
            if arr[i-1][(top[i-1]+2)%8] != arr[i][(top[i]+6)%8]:
                tlst.append((i, (i-idx)%2))
            else:       # 같은 극성이면 더이상 전달 안 됨
                break
        # [3] 좌측방향 처리
        for i in range(idx-1,0,-1):
            # 왼쪽 3시 극성 != 오른쪽 9시 극성 -> 회전 후보 추가
            if arr[i][(top[i]+2)%8] != arr[i+1][(top[i+1]+6)%8]:
                tlst.append((i, (idx-i)%2))
            else:       # 같은 극성이면 더이상 전달 안 됨
                break
        # [4] 실제 회전 처리 (시계방향 -> top -1)
        for i, rot in tlst:
            if rot == 0: # idx 톱니의 dr과 같은 방향
                top[i] = (top[i]-dr +8)%8
            else:
                top[i] = (top[i]+dr+8)%8
    ans = 0
    tbl = [0,1,2,4,8]
    for i in range(1, N+1):
        ans += arr[i][top[i]]*tbl[i]
    print(f'{tc} {ans}')