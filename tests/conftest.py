import pytest

from additional_task.task_func import User
from additional_task.task import Task
from additional_task.task_iterator import TaskItrator
from additional_task.periodic_task import PeriodicTask
from additional_task.deadline_task import DeadlineTask



@pytest.fixture
def first_user():
    return User(
        username="User",
        email="user@mail.ru",
        first_name="User",
        last_name="Userov",
        task_list=[
            Task("Купить огурцы", "Купить огурцы для салата", created_at="05.09.2024"),
            Task("Купить помидоры", "Купить помидоры для салата", created_at="05.09.2024")
        ]
    )


@pytest.fixture
def second_user():
    return User(
        username="User2",
        email="user2@mail.ru",
        first_name="User2",
        last_name="Userov2",
        task_list=[
            Task("Купить огурцы", "Купить огурцы для салата", created_at="05.09.2024"),
            Task("Купить перец", "Купить перец для салата", created_at="05.09.2024"),
            Task("Купить картошку", "Купить картошку для салата", created_at="05.09.2024")
        ]
    )


@pytest.fixture
def task():
    return Task("Купить огурцы", "Купить огурцы для салата", created_at="05.09.2024")


@pytest.fixture
def task_with_runtime1():
    return Task("Купить помидоры", "Купить помидоры для салата", created_at="05.09.2024", run_time=60)


@pytest.fixture
def task_with_runtime2():
    return Task("Купить помидоры", "Купить перец для салата", created_at="05.09.2024", run_time=70)


@pytest.fixture
def task_iterator(second_user):
    return TaskItrator(second_user)


@pytest.fixture
def task_periodic1():
    return PeriodicTask('Купить огурцы', 'Купить огурцы для салата', '01.04.2024', '01.01.2024',
                                 run_time=60, created_at="05.09.2024")


@pytest.fixture
def task_periodic2():
    return PeriodicTask('Купить помидоры', 'Купить помидоры для салата', '01.04.2024', '01.01.2024',
                                 run_time=60, created_at="05.09.2024")


@pytest.fixture
def task_deadline1():
    return DeadlineTask('Купить перец', 'Купить перец для салата', '20.04.2024',
                               run_time=60, created_at="05.09.2024")


@pytest.fixture
def task_deadline2():
    return DeadlineTask('Купить лук', 'Купить лук для салата', '20.04.2024',
                               run_time=60, created_at="05.09.2024")
