

# Класс-родитель
class Animal():

    # Конструктор для создания атрибутов отдельных экземпляров класса
    def __init__(self, name:str='bob', age:int=0):
        self.__name_obj = name
        self.__age = age

    # Getter свойства для получения значения
    @property
    def name(self) -> str:
        return self.__name_obj
    
    # Getter свойства для получения значения
    @property
    def age(self):
        return self.__age
    
    # Setter свойства для установки значения (также предназначен для проверки принимаемого значения извне)
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name_obj = value
        else:
            raise TypeError('Это не строка')

    # Setter свойства для установки значения
    @age.setter
    def age(self, value):
        if isinstance(value, int):
            self.__age = value
        else:
            raise TypeError('Это не целое значение')
        

# Класс-наследник
class Cat(Animal):
    
    # Конструктор наследника
    def __init__(self, name, age):
        super().__init__(name, age) # Вызов конструктора родителя для создания атрибутов родителя
        self.__species = 'cat' # Уникальный атрибут наследника

    # Уникальное свойство наследника
    @property
    def species(self):
        return self.__species
    
    # Уникальный метод наследника
    def say_meow():
        print('meow')
    

a = Cat('test', 6)
print(a.age)
print(a.name)
print(a.species)

a.age = 1

print(a.age)
print(a.name)
a.say_meow()
    