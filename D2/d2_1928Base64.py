T = int(input())

for t in range(1, T+1):
    str_list = list(map(str, input()))
    asi_list = []
    bin_list = []
    fin_list = []
    bin_str_list = []
    dec_list = []

    for s in str_list:
        if 'A' <= s <= 'Z':
            i = ord(s) - ord('A')
        elif 'a' <= s <= 'z':
            i = ord(s) - ord('a') + 26
        elif '0' <= s <= '9':
            i = ord(s) - ord('0') + 52
        elif s == '+':
            i = 62
        elif s == '/':
            i == 63
        asi_list.append(i)
    # 아스키코드로 변환된 리스트를 2진수로 리스트로 만들어야함. 
    # 앞에0b떼고 숫자만 & 

    for a in asi_list:
        b = bin(a)  # 0b100100
        bin_num = b[2:]  # 2진수 숫자
        bin_str_list.append(bin_num)
    temp_bin = ''.join(bin_str_list) #010010101100101010100101011110010101
    dec_list = temp_bin[0:len(temp_bin):8]
    print(temp_bin)
    print(dec_list)






'''
# input : 4 Encoded words (string)
# output : 3 Decoded words (string)
def decode():
 part1
 part2
 part3
 part4
 part5
 part6
 return
'''