import datetime
from additional_task.task import Task

def test_task_init(task):
    assert task.name == "Купить огурцы"
    assert task.description == "Купить огурцы для салата"
    assert task.status == "Ожидает старта"
    assert task.created_at == "05.09.2024"


def test_task_create():
    task = Task('Купить билеты', 'Купить билеты на самолет')
    task.name = 'Купить билеты'
    task.description = 'Купить билеты на самолет'
    task.status = 'Ожидает старта'
    task.created_at = datetime.datetime.now().date().strftime('%d.%m.%Y')


def test_task_update(capsys, task):
    task.created_at = '20.02.2024'
    message = capsys.readouterr()
    assert message.out.strip() == "Task(Купить огурцы, Купить огурцы для салата, Ожидает старта, 05.09.2024)\nНельзя изменить дату создания на дату из прошлого"

    task.created_at == datetime.datetime.now().date().strftime('%d.%m.%Y')
    assert task.created_at == datetime.datetime.now().date().strftime('%d.%m.%Y')


def test_task_str(task):
    assert str(task) == "Купить огурцы, Статус выполнения: Ожидает старта, Дата создания: 05.09.2024"


def test_task_add(task_with_runtime1, task_with_runtime2):
    assert task_with_runtime1 + task_with_runtime2 == 130

