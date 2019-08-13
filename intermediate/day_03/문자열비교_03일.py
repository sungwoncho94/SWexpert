T = int(input())

for t in range(1, T+1):
    origin = input()
    test = input()

    if origin in test:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')