## リストのスライス
リストの中から一部の要素を取り出す方法

list_a[0:2] # 1番目から2番目の値
list_a[0:4:2] # 1番目から4番目までを1つとばし
list_a[-3:] # 最後から3番目以降

## リストのメソッド
append: 値を一つ追加
extend: リストにリストを指定して拡張
insert: リストに位置を指定して値を追加
clear: リストを初期化
remove: 指定した要素をリストから削除
pop: 指定したインデックスの要素を取り出して、削除
count: 指定した値がリストに含まれている数を返す
index: 指定した値のインデックスを返す
copy: リストをそのままコピーして新たなリストを作成し、返す

## 並び替え
sort リストを並び替える(同じ型でないとエラー) sortedでもできる
reverse: リストの順番を入れ替える

## python(辞書型(ディクショナリー))
pythonでは辞書型を以下のように宣言する
dictionary = {'キー1': '値1', 'キー2': '値2'}

car ={ 'brand':'Toyota', 'model':'Prus' , 'year': 2015,}

print(car['brand]) # 取り出せなかった場合エラー
print(car.get(brand)) # 取り出せなかった場合None(値が存在しないことを表すクラス)
\# 変数['キー']または、変数.get('キー')とすることで値を取り出すことができる
上の例ではToyota

print(car.get('Model), 'Done not exist')
\# carにModelというキーが存在しない場合、Dose not exist(第二引数)を返す

car.keys() # carにキー'brand', 'model', 'year'が返される
car.values() # carの値'Toyota', 'Prius', 2015が返される
car.items() # carのキーとバリューがそれぞれ返される。



for key, value in cat.items(): # for分
    print("key: {}, value: {}".format(key,value)) # key,valueをそれぞれ取り出し、ループ内で回すことができる
    if key in car:
        print(car['key'])

cf: JavaScriptでの例
- Object.keys()
    - 指定されたオブジェクトが持つプロパティの名前の配列を、通常のループで取得するのと同じ順序で返す。 
- Object.values()
    - 指定されたオブジェクトが持つ列挙可能なプロパティの値を、for...inループで提供される場合と同じ順序で配列にして返す。
- for...in
    - キーが文字列であるオブジェクトの列挙可能なプロパティすべてに対して、継承された列挙可能プロパティも含めて、反復処理を行う。
(Synboklがキーになったものは無視する)
- Object.entries()
    - 引数に与えたオブジェクトが所有する、文字列をキーとした列挙可能なプロパティの組[key, vaule]からなる配列を返す。これはfor...inループでの反復処理と同様。
      

## python(辞書型(ディクショナリー))のメソッド
car.update({'countory': 'japan', 'prefecture': 'Aichi'})
辞書carにcountryとprefectureを値とともに追加する

car['city'] = 'Toyota-shi'
value=car.popitem()
最後に追加した要素を削除する。(この場合、city)ただし、python3.7より前では任意の値を削除する
またvalueに('city', 'Toyota')とタプルして返される

value= car.pop('prefecture')
指定したキーを削除する。また、この場合valueにはAichiが入る

car.clear()
carに入った値がすべて削除される

del car
dictionary carが削除される


## Python(タプル)
タプルとは、リストに似ていて値を複数入れる。値を変更、追加できない

fruit = ('apple', 'banana', 'orange', 'lemon')

print(fruit[0]) # タプルの1番目の要素にアクセス

fruit[0] = 'grape' # TypeError タプルは値を変更することができない

fruit = fruit + ('grape',) # タプルに要素を追加するには、+('',)として、タプル+タプルの形にする

# タプルのメソッド count, index
# タプルをリストに変換する

list_a = ['banana','apple','grape']
fruit = tupple(list_a)# ↑tupple(リスト)とすると、リストをタプルに変換することができる

リストと違う特徴は、値の変更ができないということ
{('A', 'B'): 'value'}
- 配列よりもタプルのほうが、アクセススピードが速い
- ハッシュ化して辞書型のキーとして、利用できる
- 値を変更したくないような値を用いる場合に、値は変更できないことを保障できる
(MONTH=('Jan', 'Feb',....)など)

## Python(セット)
セットはリスト[],タプル()と似たように複数の値を入れることができる
- 同じ値を持つことができない(ユニーク)
 => 重複を削除する時に使う
- 順序が保持されていない(挿入された順番通りに取り出すことができない)
- ユニオンやインターセクションなどの集合処理を高速で行うことができる

set_a = {'a','b','c','d','a'} # setを作成。'a'が2つあるが、一つしか入っていない
print(set_a) # set_aには{'a','b','c','d'}の4つの要素がある

print('e' in set_a)# set_aには,'e'が入っていないため、Falseがかえる
print('e' not in set_a) # set_aには、'e'が入っていないため、Trueがかえる
print(len(set_a)) # set_aの数を返す。この場合4が返る


set_a.add('e') # set_aに'e'を追加する
set_a.remove('e') # set_aから'e'を削除する。'e'がない場合は、KeyErrorを返す
set_a.discard('e') # set_aから'e'を削除する。'e'がない場合でも、エラーは発生しない
set_a.pop() # set_aから任意の値を取り出して返して削除する
set_a.clear() # set_aからすべての要素を削除する

cf:JavaScript
in 演算子は、指定されたプロパティが指定されたオブジェクトにある場合に true を返します。

## Python(セットのメソッド)
セットのメソッドは、以下のようなものがある

unio(|)・・・ユニオン、和集合を返す
intersection(&)・・・集合の共通する要素、積集合を返す。
difference(-)・・・片方の集合にあり、片方の集合にない要素、差集合を返す
symmetric_difference・・・どちらから一方にだけある要素の集合を返す

s = {'a', 'b', 'c', 'd' }
t = {'c', 'd', 'e', 'f' }

s | t # sとtのユニオンの集合、{'a', 'b', 'c', 'd', 'e', 'f' }を返す
s.union(t) # sとtのユニオン場合、{'a', 'b' ,'c', 'd', 'e', 'f' }を返す

s & t # sとtの積集合、{'c', 'd'}を返す
s.intersection(t) # sとtの積集合、{'c', 'd'}を返す

s - t # s.difference(t)では、sとtの差集合、{'a','b'}を返す。
s.difference(t) # sとtの差集合の場合、{'a', 'b'}

s^t # s.symmmetric_difference(t)では、sとtの片方に含まれる{'a', 'b', 'e', 'f'}を返す。
s.symmetric_difference(t) # sとtの片方に含まれる、{'a', 'b', 'e', 'f'}を返す
=> どちらか一方に含まれているけど、両方に含まれていない集合



s |= t # sとtのユニオン、つまりsにtの値を追加する
s = {'apple', 'lemon'}
t = {'apple', 'banana', 'lemon', ''grape}
u = {'cherry'}

print(s.issubset()) # sの要素はすべてtに含まれるため、sはtのサブセットでTrueを返す
print(s.issupperset(t)) # sの要素はすべてtに含まれるため、tはsのスーパーセットでTureを返す
print(s.isdisjoint(u)) # tの要素とuの要素は一つもかぶっていないため、Trueを返す

## 制御構文(if文)
if文は、渡された値の真偽を評価し、秦の場合は実行され、偽の場合は実行されない式のこと

if 評価式:
    式
とする。

pythonでは、以下の値が偽として認識される。
- None,Falas,0,""(空文字),空のリスト、空の辞書、空のセット

厳密には以下を満たすもの
- __bool__()が定義されるクラスで、Falseが返されるもの
変数.__bool__() = bool(変数)

if文を複数重ねるには、elif,elseを利用する

等価性:<,<=,>,=>,==,not
if 評価式1:
    式 # 評価式1が正の場合実行
elif 評価式2:
    式 # 評価式1が偽で、評価式2が正の場合実行
else:
    式 # 評価式1も評価式2も偽の場合実行

- and or not

複数の条件式を評価する場合、and,orを利用する。また、条件式の否定としてnotが利用される。
- 条件式1 and 条件式2とすると、条件式1と条件式2の両方が正しい場合に実行される
- 条件式1 or 条件式2とすると、条件式1と条件式2のどちらか一つが正しい場合実行される。
- not条件とすると、条件が誤っている場合に実行される

＃python(all, any関数)
if分とallとanyを利用すると処理の記載が楽になる

# allはオブジェクトの中がすべてTrueの場合処理をする
if all(反復可能オブジェクト): # リスト、タプルなど、for in でループできる変数を入れる
    処理

# anyはオブジェクトの一部がTrueの場合に処理をする
if any(反復可能オブジェクト):


# python(ループ文(for, while))
ループ文では、複数回同じコードを実行する。pythonではfor,whileを用いてループを実現する。

for 制御文:
    式 # ループ内の式が実行される

range関数(for in range()として利用)
range(5):0,1,2,3,4を返す
range(2, 6):2,3,4,5を返す
range(0,10,3):0,3,6,9

for i in range(5):
    print(i) # 0,1,2,3,4を表示

リストのループ
sample = ['A', 'B', 'C']
for s in sample:
    print(s) # A B C を表示


for _ in range(100):
    print('A')
変数に値を格納するのではなく、ただループしたいことを強調したいときに利用する

sample = ['John', 'Paul', 'George', 'Ringo']
sample = ('John', 'Paul', 'George', 'Ringo')
for member in sample:
    print(member)

human = {
    'Name': 'Taro',
    'Age': 20,
    'gender': 'Man'
}
for h in human:
    print(h, human.get(h))

# python(ループ文(for, while))
enumerate関数：配列の中の値とインデックスを同時に取得する
sample = ['A', 'B', 'C']
for index, value in enumerate(sample):
    print(index) # 0 1 2を表示
    print(value) # A B Cを表示

zip関数:二つの配列の中の値を同時に取得する
for a,b in zip(list1, list2):

while:whileの中の式がTrueであるうちは処理を実行する

count = 0;
while count < 0:
    print(count)
    count += 1


# python(ループ文(countinue, break, else))
pythonのループ内でcountinue,break,elseの使い方

countinue: ループ内にcountinueがあると処理が飛ばされる
break: breakが実行されるとループの外に処理が出る

for i in range(10):
    if == 3:
        countinue # iが3の時は、処理が飛ばされる。(i=4の場合は次の処理に移る。)
        breakの場合は処理が終了してループの外にでる
        print(i)

else: ループの外に出た際に実行される。(breakでループを抜けた場合には実行されない)

for i in range(10):
    print(i)
else:
    print('ループ終了') # ループ終了後実行される



# python(セイウチ演算子(3.8移行))
:＝イコールの前に:コロンとつけた演算子

変数の代入と変数の使用を同時に実行できるという特徴を持っている

if(n := 10) > 5:# nに10を代入するのとn > 5の比較を同時に実行している

一番よく使うパターンは、whileだろう

n = 0
whle(n := n + 1) < 10
    print(n)

n = 1
while n < 10
    print(n)
    n += 1

# Python(例外処理try, except)
例外処理：実行時に発生するエラー(実行時エラー)を制御して処理を行う

try:
    処理
except エラー内容
    例外発生時の処理

例)
try:
    a = 10 / 0
except ZeroDivisionError
    import traceback
    traceback.print_exe() # エラーの内容を表示
    pass
    print('例外処理')
except Exception as e: # すべての例外をCatch


FileNotFoundError:プログラムで指定されたファイルが見つからないエラー
IndexError: 配列などで指定したインデックスに値が存在しないエラー
TypeError:型に関するエラー
ZeroDivisionError: 0で割ろうとしたことによるエラー
Exception:すべての例外


# python(例外処理(try, catch, else, finally))
例外処理を複数つないだもの

fruits = ['apple', 'orange', 'grape']
count = 12

try:
    frtui = fruits[2]
    print(fruit, count)
except IndexError as e:
    print('配列に存在しないインデックスを指定した場合')
except TypeError:
    print('文字列型+整数型など、型の誤ったものと計算した場合などに実行')
except Exception:
    print('すべての例外をキャッチ')
else:
    処理
finalley:
    処理
else, finally:例外処理の後に実行される

else: 例外が発生しなかった場合に実行され、例外が発生した場合に実行されない
finally:例外が発生した場合にも、発生しなかった場合にも実行される

elseは処理を分けたいときに使用する。
- tryのほうはエラーをCatchして、elseの場合にはエラーが発生した場合そこでストップさせる。
- 例外はちょっと時間がかかる。重い処理はelseのほうに書きたいなど

- finallyはエラーが発生しても発生しなくても実行する。
 - tryで称した変数をfinallyブロックで初期化したい
 - tryの処理が終了したら、ログを吐き出したい

 # poython(例外を返す(raise))
 def divide(a, b):
    if(b == 0):
        raise ZeroDivisionError('bを0に設定しないでください)
    # raiseをすると呼び出しもとにメッセージとともに、例外を返すことができる
    else:
        return a / b

try:
    result = divide(10, 0)
    # 関数を呼び出した結果、ZeroDivisionErrorが返ってくる
except ZeroDivisionError as e:
    print('{}: {}'.format(type(type(e), e)))
    # ZeroDivisionErrorが発生したため、<class ZeroDivisionError>
    : bを0に設定しないでくださいと表示

try:
    code
except Exception as e:
    raise ○○ from e

class MyException(Exception) # 例外自作
Exceotion すべての例外を含んだクラスを継承する
どの例外にも該当しない場合、自分で例外を定義したいときに使用する。

