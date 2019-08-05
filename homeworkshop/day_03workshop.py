given_list = list(map(str, input()))
a = 0
TF = True

def palidrome(x):
    for a in range(0, len(given_list) // 2):
        b = a * (-1) - 1
        if given_list[a] == given_list[b]:
            TF = True
            a += 1
        else:
            TF = False
            break
    return(TF)

print(palidrome(given_list))



# 강사님 해설
def palisrome_lec(word):
	list_word = list(word)
	for i in range(len(list_word) // 2):  //  # 2로 나눈 몫을 구함
		if list_word[i] != list_word[-i-1]:
			return False
	return True
	
# 강사님 해설2
def palidrome_lec2(word):
    return word == word[::-1]    # slicing을 하는데, 단어 뒤에서부터 하나씩 자름 (거꾸로 배열)