#Task 1
class HeavenlyBody(object):
    'Родительский класс HeavenlyBody'

    def __init__(self, name, age, temperature, radius):
        self.name = name
        self.age = age
        self.temperature = temperature
        self.radius = radius

    def display(self):
        print(f'Имя: {self.name}')
        print(f'Возраст: {self.age}')
        print(f'Показатель температуры на небесном теле: {self.temperature}')
        print(f'Радиус небесного тела: {self.radius}')

class Planet(HeavenlyBody):
    'Дочерний кдасс Planet'

    def __init__(self, name, age, temperature, radius, orbital_speed):
        super().__init__(name, age, temperature, radius)
        self.orbital_speed = orbital_speed

    def display(self):
        super().display()
        print(f'Орбитальная скорость: {self.orbital_speed} \n')

class Star(HeavenlyBody):
    'Дочерний кдасс Star'

    def __init__(self, name, age, temperature, radius, constellation):
        super().__init__(name, age, temperature, radius)
        self.constellation = constellation

    def display(self):
        super().display()
        print(f'Созвездие: {self.constellation} \n')

planet1 = Planet('Земля', 4540, '16.92', 6371, '29.8')
star1 = Star('Полярная звезда', 60, '5500', 47, 'Малая Медведица')

print(Planet.__doc__, end='\n')
planet1.display()

print(Star.__doc__, end='\n')
star1.display()


#Task 2
import datetime

class Pastry(object):
    def __init__(self, name, price, manufacture_date, term):
        self.name = name
        self.price = price
        self.manufacture_date = manufacture_date
        self.term = term

    def display(self):
        print(f'Название выпечки: {self.name}')
        print(f'Цена выпечки: {self.price}')
        print(f'Дата изготовления выпечки: {self.manufacture_date}')
        print(f'Срок хранения выпечки: {self.term}')

    def valid_until(self):
        today = datetime.date.today()
        end_day = self.manufacture_date + datetime.timedelta(days=self.term)
        remaining_time = end_day - today
        if remaining_time.days < 0:
            return 'Срок годности истек'
        else:
            return 'Срок годности истекает через {} дня'.format(remaining_time.days)

class Cake(Pastry):
    'Дочерний класс Cake'

    def __init__(self, name, price, manufacture_date, term, filling):
        super().__init__(name, price, manufacture_date, term)
        self.filling = filling

    def order(self):
        def order(self):
            Cake.display(self)
            print(f'Начинка: {self.filling}')
            if Cake.valid_until(self) != 'Срок годности истек':
                print(Cake.valid_until(self))
                print(f'Оформлен заказ {self.id} - {self.name} с {self.filling} \n')
            else:
                print('Такого нету в наличии')

class BentoCake(Pastry):
    'Дочерний класс BentoCake'

    def __init__(self, name, price, manufacture_date, term, celebration):
        super().__init__(name, price, manufacture_date, term)
        self.celebration = celebration

    def order(self):
        if BentoCake.valid_until(self) != 'Срок годности истек':
            BentoCake.display(self)
            print(f'Праздник: {self.celebration}')
            print(BentoCake.valid_until(self))
            print(f'Оформлен заказ {self.name} на {self.celebration} \n')
        else:
            print('Такого нету в наличии')

cake1 = Cake('Торт', 1300, datetime.date(2023, 8, 14), 40, 'яблоко')
bento1 = BentoCake('Бенто торт', 1000, datetime.date(2023, 8, 20), 40, 'день рождения')

cake1.order()
bento1.order()

#Task 3
class BankAccount(object):
    def __init__(self, holder, balance, interest_rate):
        self.__holder = holder
        self._balance = balance
        self._interest_rate = interest_rate

    @property
    def holder(self):
        return self.__holder

    @holder.setter
    def holder(self, holder):
        self.__holder = holder

    def __str__(self):
        print(f'Владелец: {self.__holder}')
        print(f'Баланс: ${self._balance}')
        print(f'Процентная ставка: {self._interest_rate}')

class BankOperation(BankAccount):
    def __init__(self, holder, balance, interest_rate):
        super().__init__(holder, balance, interest_rate)
        self.id = id(self)
        self.transactions = []

    def deposit(self, amount):
        self._balance += amount
        self.transactions.append(f'Аккаунт {self.id} - внесение наличных на счет: {amount}$')

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            self.transactions.append(f'Аккаунт {self.id} - cнятие наличных: {amount}$')
        else:
            print('Аккаунт {self.id} - недостаточно средств на счете')

    def add_interest(self):
        interest = self._balance * self._interest_rate
        self._balance += interest
        self.transactions.append(f'Аккаунт {self.id} - начислены проценты по вкладу: {interest}$ \n')

    def history(self):
        for transaction in self.transactions:
            print(transaction)

account = BankOperation('Warren Buffett', 113000000000, 0.08)

account.__str__()
account.deposit(4000000000)
account.withdraw(88000000000)
account.add_interest()
account.history()


#Task 5
def buying_securities(func):
    def wrapper(security):
        if security.echelon == 3:
            print('Это высокорискованная сделка')
            return None
        return func(security)
    return wrapper

class Investments(object):
    def __init__(self, ticker, price, currency, industry):
        self.ticker = ticker
        self.price = price
        self.currency = currency
        self.industry = industry

    def display(self):
        print(f'Тикер: {self.ticker}')
        print(f'Цена: {self.price}')
        print(f'Валюта: {self.currency}')
        print(f'Сектор: {self.industry}')


class Shares(Investments):
    'Дочерний класс Shares'

    def __init__(self, ticker, price, currency, industry, dividend, echelon, profit):
        super().__init__(ticker, price, currency, industry)
        self.dividend = dividend
        self.echelon = echelon
        self.profit = profit

    @buying_securities
    def buying(self):
        if self.profit > 5:
            lot = int(input('Количество: '))
            print(f'Совершена покупка на сумму: {self.price * lot} \n')
        else:
            print('Годовая доходность меньше 5% в год')

class Bonds(Investments):
    'Дочерний класс Bonds'

    def __init__(self, ticker, price, currency, industry, coupon, echelon, nominal):
        super().__init__(ticker, price, currency, industry)
        self.coupon = coupon
        self.echelon = echelon
        self.nominal = nominal

    @buying_securities
    def buying(self):
        if self.price <= self.nominal:
            lot = int(input('Количество: '))
            print(f'Совершена покупка на сумму: {self.price * lot} \n')
        else:
            print('Стоимость облигации не больше ее номинальной стоимости')

i1 = Shares('GAZP', 174, 'RUB', 'Энергетика', True, 1, 6)
i1.display()
i1.buying()
i2 = Bonds('ОФЗ-26233', 688, 'RUB', 'Государственные', 6, 3, 1000)
i2.display()
i2.buying()