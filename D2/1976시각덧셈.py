T = int(input())

for t in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())

    result_hour = h1 + h2
    result_minute = m1 + m2
    
    if result_minute >= 60:
        result_minute -= 60
        result_hour += 1
    
    if result_hour > 12:
        result_hour -= 12
        
    print('#{} {} {}'.format(t, result_hour, result_minute))