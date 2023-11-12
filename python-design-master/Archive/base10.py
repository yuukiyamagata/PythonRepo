car = {'brand': 'Toyata', 'model': 'Prius', 'year': 2015, 1: 100 }
print(car['brand'])
print(car.get('bran', 12))
print(car[1])
print(car.get(1))

print(car.keys()) # キー一覧
print(car.values()) # 値一覧
print(car.items()) # キー + 値一覧

for key, value in car.items():
    print("key={}, value={}".format(key, value))


if 'brand' in car:
    print('carのブランドは {}'.format(car['brand']))