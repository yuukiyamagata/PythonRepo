# if and or not

# msg = 'yellow'
# if msg == 'blue':
#     print('すすめ')
# elif msg == 'red':
#     print('とまれ')
# else:
#     print('それ以外の処理')

age = 60

if age < 20:
    print('20未満です')
elif age <= 40: #20以上で実行される
    print('20以上40以下です')
elif age >= 60:
    print('60以上です')
else:
    print('それ以外')


gender = 'woman'
age = 40 
if gender == 'man' or  age < 20:
    print('男性もしくは20未満です')

if gender != 'man':
    print('男ではない')