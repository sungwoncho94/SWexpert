''' 가영님 코드
T = int(input())

for t in range(1, T + 1):
    p, q, r, s, w = map(int, input().split())
    A_com = w * p  # A회사 가격(언제나 동일)
    B_com = q
    if w > r:
        B_com += (w - r) * s
    if A_com <= B_com:
        print(f'#{t} {A_com}')
    else:
        print(f'#{t} {B_com}')
'''

def case_a(p, q, r, s, w):
    return(p * q)
def case_b1(p, q, r, s, w):
    return(q + (w - r)* s)
def case_b2(p, q, r, s, w):
    return(q)

T = int(input())
for t in range(1, T + 1):
    p, q, r, s, w = map(float, input().split())
    best_price = min(case_a(p,q,r,s,w), case_b1(p,q,r,s,w), case_b2(p,q,r,s,w))
    print(best_price)