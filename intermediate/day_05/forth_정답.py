import sys
sys.stdin = open("4874.txt", "r")

TC = int(input()) #테스트 횟수

for tc in range(1, TC+1):
    data = list(input().split()) #공백기준 나눈 후 리스트로 변환
    n = len(data)  #반복횟수
    stack = []
    result = 0
    errorFlag = False #예외발생여부

    for i in range(n-1): #연산식 만큼 반복
        #숫자이면 스택에 저장
        try:
            if data[i].isdigit(): #숫자냐?
                stack.append(data[i])
            else: #숫자가 아니면
                #후위표기법 계산   #    마지막_이전숫자  "연산자"  마지막숫자
                num2, num1 = int(stack.pop()),int(stack.pop())
                if data[i] == "+": result = num1 + num2
                elif data[i] == "-": result = num1 - num2
                elif data[i] == "*": result = num1 * num2
                elif data[i] == "/": result = num1 // num2

                stack.append(result)#계산결과를 스택에 저장
        except:
            errorFlag = True
        #for 끝
    if errorFlag == False and len(stack)==1:
        print("#%d %d" %(tc,stack[0]))
    elif errorFlag == True or len(stack) > 1:
        print("#%d error" % (tc))



