def notwall(new_x, new_y):
    return 0 <= new_x < 4 and 0 <= new_y < 4

def wantam(x, y, cnt, mystring): # start에서 시작해서
    # global cnt, mystring

    for _ in range(4):
        new_x = x + dx[_]
        new_y = y + dy[_]
        if notwall(new_x, new_y):
            mystring += str(arr[new_x][new_y])
            cnt += 1
            if cnt == 6: #####여기서 if cnt == 6 and if mystring not in result: 라고 하면 무한루프
                if mystring not in result:
                    result.append(mystring)
            else:
                wantam(new_x, new_y, cnt, mystring)
            mystring = mystring[:-1] #마지막 하나 빼고 더해줌
            cnt -= 1
        new_x -= dx[_]
        new_y -= dy[_]

if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        arr = [0]*4
        for i in range(4):
            arr[i] = list(map(int, input().split()))

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        cnt = 0; result = []; mystring = ''

        for i in range(4):
            for j in range(4):
                mystring += str(arr[i][j])
                wantam(i, j, cnt, mystring)
                mystring = mystring[:-1]
                # mystring = '' # max recursion cut
        print('#%d %d' % (tc,len(result)))