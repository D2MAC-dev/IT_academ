m = int(input())
h = int(input())
x = h / 100
imt = round(m / (x * x))
# 50 - 20 = 30 steps
first = round(int(imt))
print("Ваш индекс массы тела :" + "" + str(imt))
scale = '10' + "=" * first + str("|") + "="*(50 - imt) + "50"
print(scale)
