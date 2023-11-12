# 1 OK
num = 10
#2 OK
print(type(num))
#3 OK
num_str = str(num)
#4
num_list = [num_str, '20', '30']
print('num_list={}'.format(num_list))
#5OK
num_list.append('40')
#6OK
num_tupple = tuple(num_list)
#7OK
input_val = input('標準入力を受け付け、num_tuppleに追加します:')
num_tupple = num_tupple + (input_val,)
#8OK
num_set = {'40', '50', '60'}
print('num_tupple={}'.format(num_tupple))
print('num_set={}'.format(num_set))

#9Ok
print(num_set | set(num_tupple)) # 10,20,30,40,50,60, input_val
#10OK
num_dict = {num_tupple: num_str}
#11
print(len(num_list))
#12
print(num_dict.get('MyKey', 'Does not exist'))
#13
num_list.extend(['50', '60'])
print('num_list={}'.format(num_list))


#14
val = int(input('標準入力を受け付けています。数値を入力してください：'))
is_under_50 = int(val) < 50
print('is_under_50={}'.format(is_under_50))

#15
print(f'num_stt = { num_str }')
#16
print(dir(num_dict))

