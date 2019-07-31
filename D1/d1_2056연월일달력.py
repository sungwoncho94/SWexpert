T = int(input())

for t in range(1, T+1):
    input_date = input()

    if input_date[4:6] == '02':
        temp_day = int(input_date[6:8])
        if temp_day <= 28:
            print(f'#{t} {input_date[0:4]}/{input_date[4:6]}/{input_date[6:8]}')
        else:
            print(f'#{t} -1')
    elif input_date[4:6] == '04' or input_date[4:6] == '06' or input_date[4:6] == '09' or input_date[4:6] == '11':
        temp_day = int(input_date[6:8])
        if temp_day <= 30:
            print(f'#{t} {input_date[0:4]}/{input_date[4:6]}/{input_date[6:8]}')
        else:
            print(f'#{t} -1')
    elif input_date[4:6] == '01' or input_date[4:6] == '03' or input_date[4:6] == '05' or input_date[4:6] == '07' or input_date[4:6] == '08' or input_date[4:6] == '10' or input_date[4:6] == '12':
        temp_day = int(input_date[6:8])
        if temp_day <= 31:
            print(f'#{t} {input_date[0:4]}/{input_date[4:6]}/{input_date[6:8]}')
        else:
            print(f'#{t} -1')
    else:
        print(f'#{t} -1')