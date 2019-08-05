# 1번 문제
# 변경 가능한 것 : List, set, dictionary
# 변경 불가능한 것 : tuple, range, string


# 2번 문제
result = []
for r in range(1, 51):
    if r % 2 == 1:
        result.append(r)
print(result)

# 결과 : [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]

# 3번 문제

class_inf = {
        '조성원' : 26,
        '김나나' : 25,
        '이현상' : 28,
        '장지원' : 27,
}

print(class_inf)