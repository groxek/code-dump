class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def speak(self):
        print(self.sound)



class Dog(Animal):
    def __init__(self, name, age, poroda: str):
        super().__init__(name, age, 'Гав!')
        self.poroda = poroda


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, 'Мяу!')

    def speak(self):
        print('Мяу')


dog1 = Dog('lake', 4,'лайка')
dog1.speak()

cat1 = Cat('mursik', 2)
cat1.speak()

jiraf = Animal('bob', 12, 'frrrr')
jiraf.speak()


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        if balance>=0:
            self.__balance = balance
        else:
            raise ValueError('Сумма не может быть отрицательной')

    def deposit(self, amount):
        try:
            if amount>0:
                self.__balance+=amount
            else:
                print('Ошибка: сумма должна быть положительной')
        except TypeError:
            print('Нужно передать число')

    def withdraw(self, amount):
        try:
            if self.__balance >= amount:
                self.__balance -= amount
            else:
                print('Ошибка: недостаточно средств')
        except TypeError:
            print('Нужно передать число')

    def get_balance(self):
        return self.__balance

bro = BankAccount('Sanya', 2000)

print(bro.get_balance())
bro.withdraw(3000)
bro.deposit(-123)
bro.withdraw("9876")
