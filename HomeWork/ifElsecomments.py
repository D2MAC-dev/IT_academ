# request information from the user
a = int(input("Введите значение 1 : "))
b = int(input("Введите значение 2 : "))
c = int(input("Введите значение 3 : "))
result = a and b and c and "Нет нулевых значений!!!"
resilt_2 = a or b or c or "Введены все нули!!!"
print(result)
print(resilt_2)

if a > b + c:
    print("a > b + c :" + a - b - c)
elif a <= b + c:
    print(b + c - a)

if a > 50 and b > a or c > a:
    print("Вася") 

if a > 5 or b == 7 and c == 7:
    print("Петя")