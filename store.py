# Ты разрабатываешь программное обеспечение для сети магазинов.
# Каждый магазин в этой сети имеет свои особенности, но также существуют общие характеристики,
# такие как адрес, название и ассортимент товаров. Ваша задача — создать класс Store,
# который можно будет использовать для создания различных магазинов.
# Шаги:
# 1. Создай класс Store:
# -Атрибуты класса:
# name: название магазина.
# address: адрес магазина.
# items: словарь, где ключ - название товара, а значение - его цена. Например, {'apples': 0.5, 'bananas': 0.75}.
# Методы класса:
# __init__ - конструктор, который инициализирует название и адрес, а также пустой словарь дляitems`.
# метод для добавления товара в ассортимент.
# метод для удаления товара из ассортимента.
# метод для получения цены товара по его названию. Если товар отсутствует, возвращайте None.
# метод для обновления цены товара.
# 2. Создай несколько объектов класса Store:
# Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них
# несколько товаров.
# 3. Протестировать методы:
# Выбери один из созданных магазинов и протестируй все его методы:
# добавь товар, обнови цену, убери товар и запрашивай цену.

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item, price):
        self.items[item] = price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def get_price(self, item):
        if item in self.items:
            return self.items[item]
        else:
            return None

    def update_price(self, item, new_price):
        if item in self.items:
            self.items[item] = new_price


    def all_items(self):
        print(f"В магазине {self.name} по адресу {self.address} в ассортименте:")
        for key, value in self.items.items():
            print(key, value)


store1 = Store("My Store1", "12 Main St")
store1.add_item("apple", 5)
store1.add_item("banana", 7.5)
store2 = Store("My Store2", "13 Main St")
store2.add_item("ananas", 10)
store2.add_item("melon", 3)
store3 = Store("My Store3", "14 Main St")
store3.add_item("pumpkin", 2.5)
store3.add_item("turnip", 1.75)
store2.remove_item("melon")
store2.get_price("ananas")
store2.update_price("ananas", 11)
store2.add_item("cherry", 8)
store2.get_price("cherry")
store2.update_price("cherry", 8.8)
store2.all_items()
store3.all_items()
store1.all_items()