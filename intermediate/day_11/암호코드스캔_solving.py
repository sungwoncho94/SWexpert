T = int(input())

bacord_list = [[3, 2, 1, 1], [2, 2, 2, 1], [2, 1, 2, 2], [1, 4, 1, 1], [1, 1, 3, 2], [1, 2, 3, 1], [1, 1, 1, 4], [1, 3, 1, 2], [1, 2, 1, 3], [3, 1, 1, 2]]

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr_str = ''
    result = []
    arr_list = []
    end_result = 0

    for n in range(N):
        temp = str(input())

        if temp != '0' * M and temp not in arr_list:
            arr_list.append(temp)

    for x in range(len(arr_list)):
        for a in arr_list[x]:
            if a != '0':
                arr_str += a
        # print(arr_str) = '1DB176C588D26EC'

        temp = int(arr_str, 16)  # 16진수 -> 10진수
        temp_bin = str(bin(temp))  # 10진수 -> 2진수
        binary_int = temp_bin[2:]

        while binary_int[-1] == '0':
           binary_int = binary_int[:-1]

        while len(binary_int) % 7 != 0:
            binary_int = '0' + binary_int

        # print(binary_int) = 01110110110001011101101100010110001000110100100110111011

        length = len(binary_int) // 56
        cut = 7*length

        while len(binary_int) > 0:
            temp_len = binary_int[len(binary_int)-cut:]  # 7, 14, 21... 개씩 자르면서 비율 세서 리스트에 넣자
            len_list = [0] * 4
            len_list[0] += 1
            i = 0
            for tem in range(len(temp_len)-1):
                if temp_len[tem] == temp_len[tem+1]:
                    len_list[i] += 1
                else:
                    i += 1
                    len_list[i] += 1

            for idx in range(10):
                if bacord_list[idx] == len_list:
                    result.insert(0, idx)

            binary_int = binary_int[:len(binary_int)-cut]

        if len(result) == 8:
            trans_number = (result[0] + result[2] + result[4] + result[6])*3 + result[1] + result[3] + result[5] + result[7]
            if trans_number % 10 == 0:
                value = sum(result)
            else:
                value = 0
        else:
            value = 0

        end_result += value

    print('#{} {}'.format(t, end_result))


'''
16 26
00000000000000000000000000
00000000000000000000000000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
00000000000000000000000000
00000000000000000000000000
'''