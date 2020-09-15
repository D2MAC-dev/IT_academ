m = int(input())
h = int(input())
x = h / 100
imt = round(m / (x * x))
first = round(int(imt))
scale = '10' + "=" * first + str("|") + "="*(50 - imt) + "50"
print("Ваш индекс массы тела :" + "" + str(imt))
print(scale)