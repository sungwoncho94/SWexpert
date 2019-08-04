'''
10
5
1 4 7 8 0
10
15 20 8 28 16 27 17 27 10 12
15
17 22 20 21 29 6 10 25 20 4 9 21 14 26 23
20
26 25 20 1 2 16 9 24 19 11 12 28 7 20 20 12 9 2 16 13
25
7 4 9 18 7 4 13 5 7 14 3 14 15 19 4 15 11 25 12 7 14 12 4 10 23

#1 0 1 4 7 8 
#2 8 10 12 15 16 17 20 27 27 28 
#3 4 6 9 10 14 17 20 20 21 21 22 23 25 26 29 
#4 1 2 2 7 9 9 11 12 12 13 16 16 19 20 20 20 24 25 26 28 
#5 3 4 4 4 4 5 7 7 7 7 9 10 11 12 12 13 14 14 14 15 15 18 19 23 25 
'''

T = int(input())

for t in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    sort_list = sorted(num_list)
    
    result_list = [f'#{t}']
    for s in sort_list:
        result_list.append(f'{s}')
    
    for r in result_list:
        print(r, end=' ')
    
    print()