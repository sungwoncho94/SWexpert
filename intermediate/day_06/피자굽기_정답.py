import sys
sys.stdin = open("5099.txt", "r")

TC = int(input()) #테스트횟수

for tc in range(1, TC+1):
    N,M = map(int, input().split()) #화덛크기  피자갯수
    data = list(map(int, input().split())) #피자위 치즈양
    que = []
    for i in range(N): #입력된 지즈양중 화덕갯수만큼만 큐에 저장
        que.append([data[i], i]) #치즈양, 피자번호
    # print("ㅃ=", que)

    i = 0
    while len(que)!=1:
        que[0][0] //= 2 #치즈의 양을 반으로 줄임

        if que[0][0] == 0: #줄인양이 0이면
            if N+ i < M: # 화덕크기 + 삭제된 피자갯수 < 전체 치즈갯수 => 화덕에 입장대기중인 치즈있다
                que.pop(0)  #치즈가  다녹은 피자 삭제
                que.append([data[N + i], N + i]) #입장대기중인 피자 중 한개 화덕에 넣기
                i+=1 #치즈다녹은 피자갯사 증가
            elif N+i >= M:
                que.pop(0)
        else:
            que.append(que.pop(0)) #치즈양이 0보다크면 맨앞 지즈 꺼내어 맨뒤에 넣는다.

    print('#{} {}'.format(tc,que[0][1] + 1))