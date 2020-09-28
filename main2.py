# print([1,2,3,4,5])

# l = ['a', 'b', 'c', 'd']
# print(l[0])
# first = l[0]
# print(first)
# print(l[-1])

# l.append('e')
# print(l)

# l2 = [1, 2, 3, 4]
# rl = []
# # rl.append(l)
# # rl.append(l2)
# #rl.clear()

# print(rl)
# rl.extend(l)
# rl.extend(l2)
# z = rl + ['x', 'z', 'y'] 

# print(rl)
# print(z)

# ===========================================================

# l = []
# new = l
# new.append('a')
# print(new)
# # print(dir(l))
# new.append('g')
# new.append('c')
# new.append('f')
# print(new)

# sl = l.sort()
# print(sl)
# print(id(l))
# print(id(sl))


# l = ['z']
# new = l
# new.append('a')
# new.append('s')
# new.append('m')

# f = sorted(l)
# print(l)
# print(id(l))
# print(id(f))

# rl = ['h']
# rl.extend(new)
# print(rl)

# s = 'знакай шйл куда попало и ничего\nу него не видно было '
# print(s)
# print(dir(s))
# s2 = s.split()
# print(s2)

# s = ' '
# print(','.join(s2))


# children = ['arbuzov_2000', 'ivanov_2001', 'petrov_2003', 'Bubnov_2015']

# def by_year(name):
#     return name.split('_')[-1]


# print(by_year(children[0]))

# s_children = sorted(children, key=by_year)
# print(s_children)

#===============================================================
# цикл for

# children = ['arbuzov_2000', 'ivanov_2001', 'petrov_2003', 'Bubnov_2015']

# names = []

# for child_name in children:
#     surname = child_name.split('_')[0]
#     # # surname = surname.title()
#     # print(surname)
#     # break
#     if surname.startswith('i'):
#         continue

#     surname = surname.title()
#     names.append(surname)

# print(names)

# #break

#=================================================================
#словари 

dic = {'Дима': '+375297557514', 'Валя': '+375295676315'}
print(dic)

for item in dic.keys():
    print(item)


