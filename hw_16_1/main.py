from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class ProductMixin:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.__price}, {self.quantity})"


class Product(ProductMixin, BaseProduct):
    """
    Класс для описания товара в магазине
    """
    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        if quantity <= 0:
             raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__(name, description, price, quantity)  # Вызов конструктора родительского класса
        self.__price = price

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(f"Нельзя сложить объекты разных классов: {type(self).__name__} и {type(other).__name__}")
        return self.__price*self.quantity + other.__price*other.quantity

    @property
    def price(self) -> object:
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print(f"Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, new_product):
        name, description, price, quantity = new_product.values()
        return cls(name, description, price, quantity)


class Category:
    """
    Класс для категорий товара
    """
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)
        self.products_quantity = sum([product.quantity for product in self.__products])

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.products_quantity} шт."


    @property
    def products(self):
        result = [
            f"{product}\n"
            for product in self.__products
        ]
        return ''.join(result)

    @products.setter
    def products(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    def middle_price(self):
        try:
            return sum([product.price for product in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            return 0



class Smartphone(Product):
    """
    Класс для описания телефонов
    """
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """
    Класс для описания газонов
    """
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

data = [
    {
        "name": "Смартфоны",
        "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        "products": [
            {
                "name": "Samsung Galaxy C23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000.0,
                "quantity": 5
            },
            {
                "name": "Iphone 15",
                "description": "512GB, Gray space",
                "price": 210000.0,
                "quantity": 8
            },
            {
                "name": "Xiaomi Redmi Note 11",
                "description": "1024GB, Синий",
                "price": 31000.0,
                "quantity": 14
            }
        ]
    },
    {
        "name": "Телевизоры",
        "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        "products": [
            {
                "name": "55 QLED 4K",
                "description": "Фоновая подсветка",
                "price": 123000.0,
                "quantity": 7
            }
        ]
    }
]


categories = []
for category in data:
    products = []
    for product in category['products']:
        products.append(Product.new_product(product))
    category['products'] = products
    categories.append(Category(**category))

product_item = Product('Test', 'Test', 1000, 10)
product_item_2 = Smartphone('Test2', 'Test2', 2000, 10, 1.5,  'Xiaomi', 10000, 'red')
product_item_3 = LawnGrass('Test3', 'Test3', 3000, 10, 'Canada', '1 year', 'light green')



try:
    categories[0].products = 1
except TypeError:
    print('Можно добавить только объекты класса Product или его наследников (Smartphone/LawnGrass)')

categories[0].products = product_item
print( product_item.name in categories[0].products)