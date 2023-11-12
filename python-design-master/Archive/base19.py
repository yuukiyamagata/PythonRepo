# enumerate, zip, while

fruits = ['grapte', 'Pine', 'Apple']

for index, value in enumerate(fruits):
    print('index={}'.format(index))
    print('value={}'.format(value))

classA = ['Taro', 'Hanako', 'Jiro']
classB = ['Katsuo', 'Wakame', 'Taro']

for A,B in zip(classA, classB):
    print('classA student: {}'.format(A))
    print('classB student:{}'.format(B))

count = 0

while count < 10: # countが10より地位さ場合は中の処理を実行する
    print(count)
    count += 1