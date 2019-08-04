'''
3
KOREAKOREAKOREAKOREAKOREAKOREA
SAMSUNGSAMSUNGSAMSUNGSAMSUNGSA
GALAXYGALAXYGALAXYGALAXYGALAXY
#1 5
#2 7
#3 6
'''

T = int(input())
N = range(1, 11)

for t in range(1, T+1):
    result = 0
    str_list = list(input())
    for n in N:
        right = 1
        for i in range(len(str_list)-n):
            if str_list[i] != str_list[i+n]:
                right = 0
        if right == 1:
            result = n
            break

    print(f'#{t} {result}')