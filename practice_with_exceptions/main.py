class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def __add__(self, other):
        if isinstance(other, Employee):
            return self.pay + other.pay
        elif isinstance(other, (int, float)):
            return self.pay + other
        raise TypeError


if __name__ == "__main__":
    emp1 = Employee('Ivan', 'Ivanov', 50000)
    emp2 = Employee('Petr', 'Petrov', 50000)

    print(emp1 + emp2)
    print(emp1 + 10000)
    print(emp1 + "fdfdffd")
