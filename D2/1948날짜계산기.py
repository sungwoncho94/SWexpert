from datetime import date

T = int(input())
for t in range(1, T+1):
    year = 2019

    m1, d1, m2, d2 = map(int, input().split())

    date0 = date(year, m1, d1)
    date1 = date(year, m2, d2)
    result = date1 - date0
    print(f'#{t} {result.days+1}')
