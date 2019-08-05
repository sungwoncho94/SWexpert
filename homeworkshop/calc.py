def my_plus(x, y):
    try:
        result = x + y
    except:
        return '숫자만 입력해주세요'
    else:
        return result

def my_minus(x, y):
    try:
        result = x - y
    except:
        return '숫자만 입력해주세요'
    else:
        return result

def my_mul(x, y):
    try:
        result = x * y
    except:
        return '숫자만 입력해주세요'
    else:
        return result

def my_div(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        return '0으로는 나눌 수 없습니다.'
    except:
        return '숫자만 입력해주세요'
    else:
        return result