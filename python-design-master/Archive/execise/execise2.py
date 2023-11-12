
# i = 0
# while (i := i + 1)<= 100:
#     if i % 3 == 0 and i % 5 == 0:
#         print('Fizz Buzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('{}: FizzBuzz'.format(i))
    elif i % 3 == 0:
        print('{}: Fizz'.format(i))
    elif i % 5 == 0:
        print('{}: Buzz'.format(i))
    else:
        print(i)