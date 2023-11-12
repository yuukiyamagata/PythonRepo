# raise 例外自作

class MyException(Exception):
    pass

def divide(a, b):
    if b == 0:
        raise MyException('0では割り切れません')
    return a / b

try:
    c = divide(10, 0)
except ZeroDivisionError as e:
    print('{}: {}'.format(e, type(e)))


