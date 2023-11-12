# Python(関数)
決められたルールに従って入力(インプット)を受け取り、何らかの処理を行ってから
結果として別の値を出力(アウトプット)として返す、一連の処理のまとまり。
Pythonの関数は以下のように定義する。

def 関数名():
    処理

def print_hello(): # 関数の定義
    print('Hello')

print_hello() # 関数の呼び出し、Helloが表示される

関数に引数を与えるには
def 関数名(arg1, arg2):

def num_max(a, b):
    if a > b:
        return a
    else:
        return b

num = num_max(10, 20) # 大きい方の20が返ってくる
num  = num_max(b=20, a=10) # 引数を直接設定することもできる



関数のデフォルト値の指定は、以下のようにする。
def function(arg=1, arg2=100):

可変長引数: 場合に応じてその都度、引数の長さが変わるもの
*arg1のように\*を一つつけると、可変長のタプル
**arg2のように\*を二つつけると、可変長の辞書

def spam(arg1, *arg2):
    print("arg = {}, arg2={}".format(arg1, arg2)) # arg1とarg2を表示する
    print(type(arg2)) # <class 'tupple'>が表示され、arg2がタプルであることがわかる

spam(3,4,5,5)
\# 1つ目の引数はarg1,残りはarg2に4,5,5がタプルとして挿入され、"arg1=3, arg2=(4,5,5)"が表示される。

def spam(arg1, **arg2):
    print("arg1={}, arg2={}".format(arg1, arg2)) # arg1とarg2を表示する
    print(type(arg2)) # <class 'dict'>が表示され、arg2が辞書型であることがわかる。
spam(3, arg3=5, arg4=6) # "arg1=3, arg2="{'arg3': 5, 'arg4': 6}"が表示される。

複数の返り値
retrun a, b


# Python(グローバル変数)
変数には利用できる領域(名前空間)がある。別の名前空間の変数を更新することができない場合がある。例えば、以下のように関数の中から関数の外の変数を書き換えることができない。

###################################################
glonalを使わない場合 

def printAnimal():
    animal = 'cat'
    # ここで宣言した変数animalは関数の外で宣言したanimal(='dog')とは異なる変数として扱われ、この関数内のみで有効な変数です。
    (animal = 'cat'としても関数の外の変数は書き変わらない)
    print(animal)

animal = 'dog' # 関数外の変数
printAnimal()
print(animal)
このprintでは、関数の外で有効なanimal(='dog')が表示される。
上から実行した結果、cat,dogと表示される

####################################################


####################################################
globalを使った場合、変数の名前空間を広げることができる。

def printAnimal():
    global animal # animalの前に、globalをつけて、global変数として宣言するとこのanimalは関数の外までスコープが広がる。
    (同名の変数が関数の外に存在する場合は、同じ参照先になる)
    animal = 'cat'
    print(animal) # print(animal)でcatが表示される

animal = 'dog' # 関数外の変数
printAnimal()
print(animal)
\# 関数実行時にanimalの値はcatに書き換えられるため、ここでcatと表示される

####################################################



# Python(inner関数とノンローカル変数)
Pythonでは、関数内部に関数を書くことができる。これをinner関数という。
また、ノンローカル変数(nonlocal)として宣言すると、内側の関数から外側の関数で宣言された変数を書き換えられるようになる。

inner関数の書き方
def outer():
    def inner():
     # innder関数の処理
    外の関数から、inner関数を呼び出すなど、行う

noloal変数を用いたinner関数の定義
def outer():
    ourter_value = '外’
    # 外側の変数outer_value外という文字が代入されている 