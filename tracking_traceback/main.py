class MyClass:
    def func1(self):
        try:
            1 / 0
        except ZeroDivisionError:
            print('Handled ZeroDivisionError in func1')

    def func2(self):
        try:
            print(a)
        except NameError as e:
            print(f'Handled NameError in func2: {e}')
        self.func1()

    def func3(self):
        self.func2()


if __name__ == '__main__':
    my_object = MyClass()
    my_object.func3()
