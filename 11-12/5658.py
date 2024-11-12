import sys
sys.stdin = open('5658.txt', 'r')

num_16 = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    num = input()

    print(N,K)
    print(num)

    numlst = [] # 숫자 저장
    for i in range(N//4): # 포인트 옮기기(시계방향)
        # 같은 구성이 되려면 무조건 N//4회
        for j in range(N//4+1): # 나누기
            numlst.append(num[(i+j*(N//4))%N:(i+N//4+j*(N//4))%N])

    print(numlst)