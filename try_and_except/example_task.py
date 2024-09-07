try:
    a, b = input('Input number: ').split()
    a, b = int(a), int(b)
    result = a / b
except TypeError as e:
    print(e)
except ValueError as e:
    print(f'Invalid input {e}. Please enter two integers')
except ZeroDivisionError:
    print('Cannot divide by zero')
else:
    print(result)
finally:
    print('always print')



