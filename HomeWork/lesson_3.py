m = int(input("Введите Ваш вес (кг):"))
h = int(input("Введите Ваш рост (см) :"))
imt = round(int(m / (h / 100) ** 2))
scale = '10' + "=" * imt + str("|") + "="*(50 - imt) + "50"
#first = imt - 10
#scale = '10' + "=" * first + str("|") + "="*(40 - first) + "50"
print("Ваш индекс массы тела :" + "" + str(imt))
print(scale)