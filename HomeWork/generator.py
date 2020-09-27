# создаём функцию генератора "my_generator"
def my_generator():
    n = 0
    while  n < 30:
        yield n + 1
        n += 1

# если генерируемое число делится без остатка (x % y) на 3, то выводим 'Василий'
for i in my_generator():
    if i % 3:
        print(i)
    else:
        print('Василий')

