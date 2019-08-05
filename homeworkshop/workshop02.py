'''
# Problem 1

n, m = 5, 9

for v in range(m):
    for h in range(n):
        print('*', end='')
print()


# Problem 2

student = {'python' : 80, 'algorithm' : 99, 'django' : 89, 'flask' : 83}
sum_score = 0
for score in student.values():
    print(score)
    sum_score += score
print(f'평균점수 : {sum_score/len(student)}')


# Problem 3

blood_types = ['A', 'O', 'A', 'O', 'B', 'AB', 'O', 'AB', 'AB', 'O', 'B', 'AB']
class_blood_types = {}

for blood in blood_types:
    class_blood_types[blood] = blood_types.count(blood)
    
print(class_blood_types)
'''
# 1.
# n = 5; m = 9
# for height in range(m):
#         for width in range(n):
#                 print('*', end='')
#         # 가로 출력 한줄이 끝난 후, 한 줄을 띄워야 네모모양이 나옴
#         print('')

# 2.
# student = {'python' : 80, 'algorithm' : 99, 'django' : 89, 'flask' : 83}
# sum_score = 0
# for score in student.values():
#     sum_score += score
# print(f'평균점수 : {sum_score/len(student)}')

blood_dict = {
        'A' : 0,
        'B' : 0,
        'AB' : 0,
        'O' : 0,
}
blood_types = ['A', 'O', 'A', 'O', 'B', 'AB', 'O', 'AB', 'AB', 'O', 'B', 'AB']
for blood in blood_types:
        blood_dict[blood] += 1
        print(blood_dict)
print(blood_dict)