import pytest


@pytest.fixture()
def task_2_output():
    output = (
        'Создаём новый контакт Михаил Булгаков\n'
        'Создаём новый контакт Владимир Маяковский\n'
        'Михаил Булгаков — адрес: Россия, Москва, Большая Пироговская, дом 35б, кв. 6, телефон: 2-03-27, день рождения: 15.05.1891\n'
        'Владимир Маяковский — адрес: Россия, Москва, Лубянский проезд, д. 3, кв. 12, телефон: 73-88, день рождения: 19.07.1893'
    )
    return output


@pytest.fixture()
def task_3_output():
    output = (
        'Время выполнения функции: 1.0 с.\n'
        '2\n'
        'Время выполнения функции: 0.0 с.\n'
        '2\n'
        'Время выполнения функции: 1.0 с.\n'
        '4\n'
        'Время выполнения функции: 0.0 с.\n'
        '4\n'
        'Время выполнения функции: 0.0 с.\n'
        '4'
    )
    return output
