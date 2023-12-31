# Наследование

## Задача 1 

Создайте базовый класс `HeavenlyBody`, который включает в себя:

- строку документирования класса '''Родительский класс HeavenlyBody''';
- конструктор, инициализирующий атрибуты Небесных тел: `name`, `age`, `temperature` и `radius` (название, возраст, температура и радиус объекта);
- метод `display()` для отображения свойств объекта.

Затем добавьте два подкласса `Planet` и `Star`, которые наследуют методы и свойство от класса `HeavenlyBody`, и кроме того, имеют свои атрибуты. 

Подкласс `Planet`: 
- содержит строку документирования класса '''Дочерний класс Planet''';
- содержит конструктор, инициализирующий дополнительно атрибут `orbital_speed` (орбитальная скорость);
- переопределяет метод `display()` для отображения полного набора свойств класса. 

Подкласс `Star`: 
- содержит строку документирования класса '''Дочерний класс Star''';
- содержит конструктор, инициализирующий дополнительно атрибут `constellation` (созвездие);
- переопределяет метод `display()` для отображения полного набора свойств класса.

Выведите на экран строки документации дочерних классов, затем метод `display()` для отображения свойств каждого объекта.

**Пример использования:**
```python
planet1 = Planet('Земля', 4540, '16.92', 6371, '29.8')
star1 = Star('Полярная звезда', 60, '5500', 47, 'Малая Медведица')

print(Planet.__doc__, end='\n')
planet1.display()

print(Star.__doc__, end='\n')
star1.display()
```

**Вывод:**
```
Дочерний класс Planet
Название: Земля
Возраст: 4540 (млн. лет)
Температура: 16.92 (С)
Радиус: 6371 (км)
Орбитальная скорость: 29.8 (км/с) 

Дочерний класс Star
Название: Полярная звезда
Возраст: 60 (млн. лет)
Температура: 5500 (С)
Радиус: 47 (км)
Созвездие: Малая Медведица 
```

## Задача 2

Совсем недавно Вы решили открыть кондитерский бизнес. В настоящее время Ваш магазин кондитерских изделий обрел большое количество клиентов. Ежедневно кондитеры выпекают более тонны выпечки, поэтому требуется внимательно отслеживать каждый заказ и срок годности выпечки. 

Для начала создайте базовый класс `Pastry`, который содержит: 

- конструктор, инициализирующий атрибуты кондитерских изделий: `name`, `price`, `manufacture_date` и `term` (наименование, цена, дата изготовления и срок хранения);
- метод `display()` для отображения информации о выпечке;
- метод `valid_until()`, который позволяет вычислить количество дней до истечения срока годности рассматриваемого изделия.

Торты и бенто-торты - это самые популярные позиции кондитерской. Добавьте два дочерних класса `Cake` и `BentoCake`, которые наследуют все свойства и методы от класса `Pastry`, и кроме того, имеют свои атрибуты. 

Подкласс `Cake` содержит атрибут `filling` (начинка). Подкласс `BentoCake` содержит атрибут `celebration` (праздник). Метод `order()` в дочерних классах выводит полную информацию о выпечке и осуществляет проверку срока годности. Если изделие свежее, тогда можно оформить заказ. 

**Пример использования:**
```python 
cake1 = Cake('Торт', 1300, datetime.date(2023, 7, 20), 3, 'вишня')
bento1 = BentoCake('Бенто торт', 1000, datetime.date(2023, 7, 20), 4, 'день рождения')

cake1.order()
bento1.order()
```

**Вывод:**
```
Название: Торт
Цена: 1300 (руб.)
Дата изготовления: 2023-07-20
Начинка: вишня
Срок годности истекает через 3 дня
Оформлен заказ 2150189619152 - Торт с начинкой вишня 

Название: Бенто торт
Цена: 1000 (руб.)
Дата изготовления: 2023-07-20
Праздник: день рождения
Срок годности истекает через 4 дня
Оформлен заказ 2150189619792 - Бенто торт на день рождения
```

## Задача 3
  
Создайте базовый класс `BankAccount`, который:

- содержит конструктор, инициализирующий атрибуты Банковских аккаунтов: приватный атрибут: `holder` (владелец), публичные: `balance` и `interest_rate` (баланс и процентная ставка);
- содержит getter и setter для приватного атрибута;
- переопределяет магический метод `__str__()`.

Затем добавьте дочерний класс `BankOperation`, который наследует все свойства и методы от класса `BankAccount`, и кроме того, имеет свои методы и атрибуты:

- `deposit(amount)` добавляет сумму к балансу и регистрирует транзакцию;
- `withdraw(amount)` вычитает сумму из баланса и записывает транзакцию;
- `add_interest()` добавляет проценты к счету на основе `interest_rate` и записывает транзакцию
- `history()` печатает список всех операций по счету.

**Пример использования:**
```python
account = BankOperation('Warren Buffett', 113000000000, 0.08)

account.__str__()
account.deposit(4000000000)
account.withdraw(88000000000)
account.add_interest()
account.history()
```

**Вывод:**
```
Владелец: Warren Buffett
Баланс: $113,000,000,000.00
Процентная ставка: 0.08 

Аккаунт 2289924818704 - внесение наличных на счет: $4,000,000,000.00
Аккаунт 2289924818704 - cнятие наличных: $88,000,000,000.00
Аккаунт 2289924818704 - начислены проценты по вкладу: $2,320,000,000.00
```

## Задача 4

В большинстве случаев в программировании лучше избегать сложных конструкций. В программе ниже представлена визуализация множественного ромбовидного наследования по MRO. Класс `Copier` унаследовал функциональность более чем одного класса. Изучите программу, написанную ниже, и постарайтесь ответить на вопросы: 

1. Почему каждый метод `__init__` вызывался только один раз? 
2. Почему каждый метод `__init__` был запущен до того, как любой из других был завершен?

```python
class ComputerDevice:
    '''Request process'''

    def __init__(self, inf):
        print('Start init ComputerDevice.__init__()')
        self.inf = inf
        print('End init ComputerDevice.__init__()')

class Scanner(ComputerDevice):
    '''Scan information'''

    def __init__(self, inf):
        print('Start init Scanner.__init__()')
        super().__init__(inf)
        print('End init Scanner.__init__()')


class Printer(ComputerDevice):
    '''Print information'''

    def __init__(self, inf):
        print('Start init Printer.__init__()')
        super().__init__(inf)
        print('End init Printer.__init__()')


class Copier(Scanner, Printer):
    '''Copy process'''

    def __init__(self, inf):
        print('Start init Copier.__init__()')
        super().__init__(inf)
        print(f'Отсканированная информация: {self.inf.upper()}')
        print('End init Copier.__init__()')

print(Copier.__mro__)
```

**Пример использования:**
```python
c = Copier('Hello world!')
```

**Вывод:**
```python
Start init Copier.__init__()
Start init Scanner.__init__()
Start init Printer.__init__()
Start init ComputerDevice.__init__()
End init ComputerDevice.__init__()
End init Printer.__init__()
End init Scanner.__init__()
Отсканированная информация: HELLO WORLD!
End init Copier.__init__()
```

## Задача 5

Определите базовый класс `Investments`, который включает в себя:

- конструктор, инициализирующий атрибуты ценных бумаг: `ticker`, `price`, `currency`, `industry` (тикер, цена, валюта, сектор);
- метод `display()` для отображения свойств. 

Затем создайте два дочерних класса `Shares` и `Bonds`, которые наследуют атрибуты и методы родительского класса `Investments`, и обладают собственными методами.

Подкласс `Shares` (Акции): 

- содержит конструктор, инициализирующий дополнительно атрибуты `dividend`, `echelon`, `profit` (дивиденды, эшелон, годовая доходность);
- метод `buying()`, который позволяет совершить покупку, если годовая доходность бумаги больше 5%.

Подкласс `Bonds` (Облигации): 

- содержит конструктор, инициализирующий дополнительно атрибуты `coupon`, `echelon`, `nominal` (купоны, эшелон, номинальная стоимость);
- метод `buying()`, который позволяет совершить покупку, если стоимость облигации не больше ее номинальной стоимости. 

Помимо этого, реализуйте декоратор `buying_securities`, который проверяет эшелон ценной бумаги. Если акция или облигация принадлежит к третьему эшелону, то выведите сообщение `Это высокорискованная сделка.`

**Пример использования:**
```python
i1 = Shares('GAZP', 174, 'RUB', 'Энергетика', True, 1, 6)
i1.display()
i1.buying()
i2 = Bonds('ОФЗ-26233', 688, 'RUB', 'Государственные', 6, 1, 1000)
i2.display()
i2.buying()
```

> Данная информация не является индивидуальной инвестиционной рекомендацией, и финансовые инструменты либо операции, упомянутые в ней, могут не соответствовать Вашему инвестиционному профилю и инвестиционным целям (ожиданиям).

**Вывод:**
```
Тикер: GAZP
Цена: 174
Валюта: RUB
Сектор: Энергетика
Количество: 15
Совершена покупка на сумму: 2610. Поздравляю, Вы стали совладельцем компании!

Тикер: ОФЗ-26233
Цена: 688
Валюта: RUB
Сектор: Государственный
Количество: 5
Совершена покупка на сумму: 3440. Поздравляю, Вы стали кредитором компании!
```
