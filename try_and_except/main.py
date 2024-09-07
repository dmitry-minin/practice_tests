try:
    print(a)
except NameError:
    print("NameError: name 'a' is not defined")

try:
    1/0
except ZeroDivisionError:
    print("division by zero is not allowed")

try:
    open('unknown file')
except FileNotFoundError:
    print("FileNotFoundError: 'unknown file' not found")