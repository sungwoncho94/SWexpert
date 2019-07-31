N = int(input())
num_list = list(map(int, input().split()))
sorted_list = sorted(num_list)

i = round((N + 1) / 2) - 1


print(sorted_list[i])