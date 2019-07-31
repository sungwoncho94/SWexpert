T = int(input())

for t in range(1, T+1):
    N = int(input())  # 카드 수
    card = list(input())

    # card를 int형식 list로 만들기
    card_num = []
    for c in card:
        card_num.append(int(c))
    
    # N개의 0 리스트 만들기
    count_list = [0] * 10

    # 카드 숫자에 따라 count index를 1씩 추가 = 카드 번호 숫자 세기
    for i in card_num:
        count_list[i] += 1
    
    # 카드 번호와 숫자 딕셔너리 만드기
    card_dict = dict(zip(range(10), count_list))
    max_count = max(card_dict.values())
    
    # 카드 개수가 많은 숫자를 리스트로 구하기
    max_num_list = []
    for num, count in card_dict.items():
        if count == max_count:
            max_num_list.append(num)
    
    if len(max_num_list) == 1:
        result_num = max_num_list[0]
        result_count = max_count
    else:
        result_num = max(max_num_list)
        result_count = max_count

    print(f'#{t} {result_num} {result_count}')

