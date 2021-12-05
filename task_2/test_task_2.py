import pytest
from author import mike as author_mike
from author import vlad as author_vlad
from precode import Contact, vlad
import precode


def send_msg_value_error(property, object):
    return f"Неверное значение свойства {property} у объекта {object}"


class TestTask_2:

    def test_class_exist(self):
        try:
            import precode
        except ImportError:
            assert False, 'Не найден модуль precode'
        assert hasattr(precode, "Contact"), "Не найден класс Contact"

    def test_show_contact(self):
        assert hasattr(Contact, "show_contact"), "У класса Contact отсутствует метод show_contact"

    def test_mike_attribute(self):
        try:
            from precode import mike
        except ImportError:
            assert False, 'Отсутствует объект mike'
        assert mike.name == author_mike.name, send_msg_value_error("name", "mike")
        assert mike.phone == author_mike.phone, send_msg_value_error("phone", "mike")
        assert mike.birthday == author_mike.birthday, send_msg_value_error("birthday", "mike")
        assert mike.address == author_mike.address, send_msg_value_error("address", "mike")

    def test_vlad_attribute(self):
        try:
            from precode import vlad
        except ImportError:
            assert False, 'Отсутствует объект vlad'
        assert vlad.name == author_vlad.name, send_msg_value_error("name", "vlad")
        assert vlad.phone == author_vlad.phone, send_msg_value_error("phone", "vlad")
        assert vlad.birthday == author_vlad.birthday, send_msg_value_error("birthday", "vlad")
        assert vlad.address == author_vlad.address, send_msg_value_error("address", "vlad")

    def test_print_contact(self):
        assert not hasattr(precode, "print_contact"), "Функция print_contact не удалена"

    def test_output(self, task_2_output):
        mike_show_contact = "Михаил Булгаков — адрес: Россия, Москва, Большая Пироговская, дом 35б, кв. 6, телефон: 2-03-27, день рождения: 15.05.1891"
        vlad_show_contact = "Владимир Маяковский — адрес: Россия, Москва, Лубянский проезд, д. 3, кв. 12, телефон: 73-88, день рождения: 19.07.1893"
        assert mike_show_contact in task_2_output, "Обратитесь к методу show_contact() объекта mike"
        assert vlad_show_contact in task_2_output, "Обратитесь к методу show_contact() объекта vlad"
