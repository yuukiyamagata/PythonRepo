# タプル

fruit = ('banana', 'apple', 'lemon')
print(fruit[0])
print(type(fruit))

# fruit[1] = 'grapte'
fruit = fruit + ('grapte',)
print(fruit)

list_fruit = ['apple', 'banana']
fruit = tuple(list_fruit)
print(fruit)

print(fruit.count('apple'))
# print(fruit.index('aple'))
pos = (135, 35)
countries = {pos: 'Japan'}
print(countries.get(pos))