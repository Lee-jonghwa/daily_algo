import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())

for tc in range(1, T+1):
    day, month_1, month_3, year = map(int, input().split())
    # 1~12월로 맞추기
    plans = [0] + list(map(int, input().split()))

    result = 0

    # 가장 적게 지출하는 경우
    # 매월마다 가격을 비교해야 하므로 -> DP로 하기
    # 해당하는 월에서 돈을 기준

    dp = [0] * 25 # 1~12월

    # 초기 설정
    dp[1] = min(day * plans[1], month_1)
    # dp돌리기
    for i in range(2, 13):
        if i <= 3:
            dp[i] = min(dp[i-1]+(day*plans[i]), dp[i-1]+month_1, month_3)
        elif i == 12:
            dp[i] = min(dp[i-1]+(day*plans[i]), dp[i-1]+month_1, dp[i-3]+month_3, year)
        else:
            dp[i] = min(dp[i-1]+(day*plans[i]), dp[i-1]+month_1, dp[i-3]+month_3)

    result = dp[12]
    print(f'#{tc} {result}')