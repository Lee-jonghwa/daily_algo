import sys
sys.stdin = open('1248_input.txt', 'r')

def go_up(s,path):
    for w in up_adjL[s]:
        path.append(w)
        go_up(w,path)
    return path

def go_down(s):
    global cnt
    for w in down_adjL[s]:
        cnt+=1
        go_down(w)

T = int(input())
for tc in range(1,T+1):
    inputs = list(map(int, input().split()))
    V = inputs[0]
    E = inputs[1]
    start_node_1 = inputs[2]
    start_node_2 = inputs[3]
    up_adjL = [[] for _ in range(V+1)]
    down_adjL = [[] for _ in range(V+1)]
    Es = list(map(int, input().split()))
    for j in range(E): # 간선 연결
        a, b = Es[2*j], Es[2*j+1]
        # 자식이 주어지므로, 자식에서 부모로 올라가기
        up_adjL[b].append(a)
        down_adjL[a].append(b)

    # 공통 조상을 찾는다
    lst1 = go_up(start_node_1,[])
    lst2 = go_up(start_node_2,[])

    for i in range(-1,-max(len(lst1),len(lst2)),-1): # lst를 역순으로
        if len(lst1)>len(lst2) and i<= -(len(lst2)):
            if lst1[i] != lst2[0]:
                common_a = lst1[i+1]
                break
        elif len(lst1)<=len(lst2) and i<= -(len(lst1)):
            if lst1[0] != lst2[i]:
                common_a = lst2[i+1]
                break
        elif lst1[i] != lst2[i]: # 다르면
            common_a = lst1[i+1]
            break

    cnt = 1
    # 공통조상에서 역으로 돌아간다...?
    go_down(common_a)

    print(f'#{tc} {common_a} {cnt}')


