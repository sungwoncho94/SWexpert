T = int(input())

for t in range(1, T+1):
    N = int(input())  # 운행시간(sec)

    a_list = []; s_list = []
    for n in range(N):
        try:
            act, spd = map(int, input().split())
            a_list.append(act)
            s_list.append(spd)
        except ValueError:
            # action에 0 값이 저장되지 않고 끝났기 때문에 0을 넣어줘야함
            a_list.append(0)  # [1, 1, 2, 0, 0] 
            s_list.append(0)  # [2, 2, 1, 0, 0]
    
    distance = 0  # 차가 간 거리
    speed = 0  # 현재 속도
        
    for i in range(len(a_list)):
        if a_list[i] == 1:  # 가속
            speed += s_list[i]
            distance += speed
        elif a_list[i] == 2:  # 감속
            speed -= s_list[i]  # 이전 스피드에서 이번 스피드만큼 뺀다
            if speed <= 0:
                speed = 0
            else:
                speed = speed
                distance += speed
        else:  # 현재 속도 유지
            speed = speed
            distance += speed
    print(f'#{t} {distance}')
    
        
            


    '''
    for i in range(len(a_list)):
        if a_list[i] == 1:
            speed += s_list[i]
        elif a_list[i] == 2:
            speed -= s_list[i]
            if s_list[i] >= speed:
                speed = speed
        else:
            speed = speed
        
        distance += speed
        if distance <= 0:
            distance = 0
        print(f'속도 = {distance}')
    '''
    #print(f'#{t} {distance}')
    
'''
25
2 1
2 1
0
0
0
1 2
0
2 2
1 2
2 1
1 1
2 1
0
0
0
1 1
1 2
0
0
1 2
2 2
0
2 2
0
1 1
30
2 1
2 2
2 2
1 1
1 2
2 1
0
1 1
0
0
1 2
1 2
2 1
0
0
2 2
2 1
1 2
0
1 1
2 2
1 2
2 2
0
1 2
2 1
2 2
0
1 1
2 2
#9 48
#10 111
'''