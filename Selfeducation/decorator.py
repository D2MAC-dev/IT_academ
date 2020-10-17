# def zhopa(name):
#     print(f'{name}, у тебя большая жопа')

# zhopa('Маша')


# def my_function(Firstname, lastname, age = 18 , weight= 78):
#     print('My name is {}'.format(Firstname))
#     # print(f'My name is {Firstname}')
#     print('My lastname is {}'.format(lastname))
#     print('My age is {}'.format(age))
#     print('My weight is {}'.format(weight))


# my_function('Жора', 'Васильев', 24)
   

# def my_func(name, age, *args, **kwargs):
#     print(name)
#     print(age)
#     print(args)
#     print(kwargs)
   


# a = my_func(2, 4, 100, 11, a = '3', test = 'qweqr', test1 = 'qweqweqew')

# def my_func(Firstname, lastname,age = 10 , weight= 78):
#     if age > 15:
#         return 'Your age long enoth'
#     return 'Your age have to grow up'

# a = my_func('Жора','Васильев', 17)
# print(a)

# a = my_func('Жора','Васильев')
# print(a)


# def sum(a):
#     def helper(b):
#         return a + b
#     return helper

# sum_10 = sum(10)
# print(sum_10(50))


# def grid(name):
#     #name = "Хер"
#     def helper(direction):
#         return name + ' ' + direction
#     return helper

# name = grid('Хер')
# print(name('с горы'))

# def mul(a):
#     def helper(b):
#         return a * b
#     return helper

# mult_20 = mul(20)
# a = mult_20(2)
# print(a)


# def say_hi(name):
#     return f'Hi {name}'

# def be_ho(name):
#     return f'Yo {name}, Ho!'

# def greet_mike(greeter_func, name):
#     return greeter_func(name)

# print(greet_mike(say_hi, 'Жорик'))

# def dec(func):

#     def wrapper_decorator(*args, **kwargs):

#         value = func(*args, **kwargs)

#         return value

#     return wrapper_decorator

# def zhopa(func):
#     def wrapper_decorator(*args, **kwargs):
#                 value = func(*args, **kwargs)
#         return value
#     return wrapper_decorator


# @zhopa
# def my_fun(name):
#     print(f'Hello {name}')

# my_fun('Маша')

# from datetime import datetime

# def timeit(func):
#     def wrapper_decorator():
#         start = datetime.now()
#         value = func()
#         print(datetime.now() - start)
#         return value
#     return wrapper_decorator


# @timeit
# def count():
#     # start = datetime.now()
#     l = []
#     for i in range(10**5):
#         if i % 2 == 0:
#             l.append(i)
#     # print(datetime.now() - start)
#     return l

# count()


# def my_func(name):
#     print(f'Hello {name}')

# def zhopa(func):
#     def wrapper_decorator(*args, **kwargs):
#         args = (args[0] + ' у тебя такая жопа',)

#         value = func(*args, **kwargs)

#         return value

#     return wrapper_decorator


# @zhopa
# def my_func(name):
#     print(f'Hello {name}')


# my_func('Маша')

def order(sentence):
    a = sentence.rfind('1')
    [print(a)]
    return

order("is2 Thi1s T4est 3a")

