# class Dog:
   
#     def __init__(self, name, age):  # метод иницииализации
#         self.name = name
#         self.age = age

# d = Dog("Лорд", 3)
# d1 = Dog("Тузик", 4)
# j = Dog("Жучка", 28)

# print(d.name)
# print(d.age)
# print(j.name)
# print(d1.name)
# print(d1.age)

# # dog = Dog()
# # dog1 = Dog()

# # dog.age = 5
# # dog.name = 'Шарик'

# # dog1.age = 4

class Dog:
    paws = 4
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def bark(self, times):
        print(f'{self.name} barks {times} times has age of {self.age}')

    def run(self):
        print(f'{self.name} runs')
        self.bark(4)

d = Dog('Шарик', 27)

print(d.age)
print(d.run())












