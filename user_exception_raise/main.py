class ShellException(Exception):
    def __init__(self, *args, **kwargs):
            self.message = args[0] if args else "Ошибкаобработки скрипта"

    def __str__(self):
        return self.message


class ShellEmptyException(ShellException):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Скрипт пустой"


class ShellShebungException(ShellException):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Отсутствует Shebang"


class ShellScript:
    def __init__(self, content):
        if not content:
            raise ShellEmptyException()
        elif content[0:2] != '#!':
            raise ShellShebungException()
        self.eval()


    def eval(self):
        pass


if __name__ == '__main__':
    bash_content = ''
    try:
        shell_script = ShellScript(bash_content)
    except ShellEmptyException as e:
        print(e)
        print("Передайте не пустой файл скрипта")
    except ShellShebungException as e:
        print(e)
        print("Валидация на Shebang не пройдена")
