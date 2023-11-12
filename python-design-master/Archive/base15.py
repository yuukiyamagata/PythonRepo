
class ClassA():

    def __init__(self, a) -> None:
        self.a = a
    
    def __bool__(self):
        if self.a == 'a':
            return True
        return False




var = ClassA('b')
print('bool関数の計算結果{}'.format(bool(var)))

if var:
    print('if文の中の処理')