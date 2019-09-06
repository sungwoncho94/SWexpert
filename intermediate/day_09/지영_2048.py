def notwall(new_x, new_y):
    return 0 <= new_x < N and 0 <= new_y < N


def zeroleft(x, y):
    global arr
    if arr[x][y] == 0:
        for i in range(y, N, 1):
            for j in range(i, N, 1):
                if notwall(x, j):
                    if arr[x][j] != 0 and arr[x][i] == 0:
                        arr[x][i] = arr[x][j]
                        arr[x][j] = 0


def left():
    global arr
    for x in range(N):
        for y in range(N):

            zeroleft(x, y)

            if notwall(x, y - 1):
                if arr[x][y] == arr[x][y - 1] and (x, y) not in visited:
                    arr[x][y] = arr[x][y] * 2
                    arr[x][y - 1] = 0

                    zeroleft(x, y - 1)

                    visited.append((x, y))
    return arr


def zeroright(x, y):
    global arr
    if arr[x][y] == 0:

        for i in range(y, -1, -1):
            for j in range(i, -1, -1):
                if notwall(x, j):
                    if arr[x][j] != 0 and arr[x][i] == 0:
                        arr[x][i] = arr[x][j]
                        arr[x][j] = 0


def right():
    global arr
    for x in range(N):
        for y in range(N - 1, -1, -1):

            zeroright(x, y)

            if notwall(x, y + 1):
                if arr[x][y] == arr[x][y + 1] and (x, y) not in visited:
                    arr[x][y + 1] = arr[x][y] * 2
                    arr[x][y] = 0

                    zeroright(x, y)
                    visited.append((x, y + 1))
    return arr


def zerodown(x, y):
    global arr
    if arr[x][y] == 0:
        for i in range(x, -1, -1):
            for j in range(i, -1, -1):
                if notwall(j, y):
                    if arr[j][y] != 0 and arr[i][y] == 0:
                        arr[i][y] = arr[j][y]
                        arr[j][y] = 0


def down():
    global arr
    for x in range(N - 1, -1, -1):  ####
        for y in range(N):

            zerodown(x, y)

            if notwall(x + 1, y):
                if arr[x][y] == arr[x + 1][y] and (x, y) not in visited:
                    arr[x][y] = arr[x][y] * 2
                    arr[x + 1][y] = 0

                    zerodown(x + 1, y)

                    visited.append((x, y))
    return arr


def zeroup(x, y):
    global arr
    if arr[x][y] == 0:
        for i in range(x, N, 1):
            for j in range(i, N, 1):
                if notwall(j, y):
                    if arr[j][y] != 0 and arr[i][y] == 0:
                        arr[i][y] = arr[j][y]
                        arr[j][y] = 0


def up():
    global arr
    for x in range(N):
        for y in range(N):

            zeroup(x, y)

            if notwall(x - 1, y):
                if arr[x][y] == arr[x - 1][y] and (x, y) not in visited:
                    arr[x - 1][y] = arr[x][y] * 2
                    arr[x][y] = 0

                    zeroup(x, y)

                    visited.append((x - 1, y))
    return arr


if __name__ == '__main__':
    T = int(input())
    for tc in range(1, T + 1):
        N, where = input().split()
        N = int(N)
        arr = [0] * N
        for i in range(N):
            arr[i] = list(map(int, input().split()))

        visited = []

        # 행 기준
        if where == 'up':
            result = up()

        if where == 'left':
            result = left()

        if where == 'right':
            result = right()

        if where == 'down':
            result = down()

        print('#%d' % tc)
        for i in range(N):
            temp = result[i]
            string = ''
            for t in temp:
                string += str(t)
                string += ' '
            print(string)