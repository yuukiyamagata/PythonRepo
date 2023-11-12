# 1
num = 10
# 2
print(type(num))
# 3
num_str = str(num)
# 4
num_list = [num_str, '20', '30']
# 5
num_list.append('40')
# 6
num_tuple = tuple(num_list)
# 7
result = input('入力した値をtuppleに追加します。値を入力してください: ')
num_tuple = num_tuple + (result,)
print('入力された後のタプルです', num_tuple)
# 8
num_set = { '40', '50', '60' }
# 9
x = num_set | set(num_tuple) # 10, 20, 30, 40, 50, 60, result 
print(x)
# 10
num_dict = {num_tuple: num_str}
print(num_dict)
# 11
length = len(num_list)
# 12

# 13

# 14

# 15
num_str = {num_str}

# 16
print(num_dict)





