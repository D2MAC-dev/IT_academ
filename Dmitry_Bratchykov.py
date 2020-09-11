#Выводим в консоль исходную строку
task = "Не знаю, как там в Лондоне, я не была. "\
       "Может, там собака — друг человека. А у нас управдом — друг человека!"
print("Выводим исходную сроку: " + task)


#Cчитаем количество символов
print("Количество символов в строке: " + str(len(task)))


#Разворачиваем строку
revers_task = task[::-1]
print("Вывод развёрнутой строки: " + revers_task)


#Выводим каждое слово с прописной буквы
print("Вывод текста прописными буквами: " + task.title())


#Находим число вхождений "нд", "ам", "о" в строку
index_nd = task.count("нд")
index_am = task.count("ам")
index_o = task.count("о")
print("'ам " + "больше чем " + "'о' :" + str(index_am > index_o))
print("'нд " + "меньше чем " + "'ам' :" + str(index_nd < index_am))
print("'о " + "больше чем " + "'нд' :" + str(index_o > index_nd))


#создаём список из строки и выводим с 1-го по 5-й индекс 
splitted = task.split(" ")
print(splitted)
print(splitted[0:5])


#Производим замену слова
chagne_city = task
print(chagne_city.replace("Лондон", "Минск"))


#Пример сложения строк Конкатенация
s1 = "Не знаю, как там в Лондоне, я не была."
s2 = "Может, там собака — друг человека."
s3 = "А у нас управдом — друг человека!"
s4 = s1 + " " + s2 + " " + s3
print("Пример сложения строк Конкатенация: " + s4)


a = task.find("Н")
b = task.rfind("а")
print(a)
print(b)

c = task.swapcase()
print(c)

d = task.startswith("Не")
e = task.endswith("d")
print(d, e)

g = task.rsplit(maxsplit=2)
print(g)

#str.rjust
text = 'Бинарный поиск — '
print(text.ljust(45),"классический рекурсивный алгоритм")

#str.strip()
text = "    tom    "
text = text.strip()
print(text)

#очередной коммент