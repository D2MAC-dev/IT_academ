
while True:
    username = input("Укажите Ваше имя:")
    if username == 'q':
        break
    else:
        h = int(input("Укажите Ваш рост (см):"))
        w = int(input("Укажите Ваш вес (кг):"))
        a = input("Укажите Ваш возраст: ")
        g = input("Укажите Ваш пол (муж / жен): ")
        user = {username : {"height" : h, "weight" : w, "age" : a, "gender" : g}}
        imt = round(int(w / (h / 100) ** 2))
        scale = '10' + "=" * imt + str("|") + "="*(50 - imt) + "50"
        print("Ваш индекс массы тела :" + "" + str(imt))
        print(scale)
        if imt <= 19:
            print("надо есть больше")
        if 20 <= imt <= 25:
            print("ешь то что ел")
        if 26 >= imt >= 35:
            print("пора худеть")
        if imt > 36:
            print("я бы перестал есть")
print(dict.get(keys))
print("end")

