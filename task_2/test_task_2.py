import pytest
from author import mike as author_mike
from author import vlad as author_vlad
from precode import Contact, mike, vlad


class TestClass:

    def test_class_exist(self):
        try:
            import precode
        except ImportError:
            assert False, 'Не найден модуль precode'
        assert hasattr(precode, "Contact"), "Не найден класс Contact"

    def test_show_contact(self):
        assert "show_contact" in dir(Contact), "У класса Contact отсутствует метод show_contact"

    def test_mike_attribute(self):
        try:
            from precode import mike
        except ImportError:
            assert False, 'Отсутствует объект mike'
        assert mike.name == author_mike.name, "Неверное значение свойства name у объекта mike"
        assert mike.phone == author_mike.phone, "Неверное значение свойства phone у объекта mike"
        assert mike.birthday == author_mike.birthday, "Неверное значение свойства birthday у объекта mike"
        assert mike.address == author_mike.address, "Неверное значение свойства address у объекта mike"

    def test_vlad_attribute(self):
        try:
            from precode import vlad
        except ImportError:
            assert False, 'Отсутствует объект mike'
        assert vlad.name == author_vlad.name, "Неверное значение свойства name у объекта vlad"
        assert vlad.phone == author_vlad.phone, "Неверное значение свойства phone у объекта vlad"
        assert vlad.birthday == author_vlad.birthday, "Неверное значение свойства birthday у объекта vlad"
        assert vlad.address == author_vlad.address, "Неверное значение свойства address у объекта vlad"

    def test_output(self, task_2_output):
        mike_show_contact = "Михаил Булгаков — адрес: Россия, Москва, Большая Пироговская, дом 35б, кв. 6, телефон: 2-03-27, день рождения: 15.05.1891"
        vlad_show_contact = "Владимир Маяковский — адрес: Россия, Москва, Лубянский проезд, д. 3, кв. 12, телефон: 73-88, день рождения: 19.07.1893"
        assert mike_show_contact in task_2_output, "Обратитесь к методу show_contact() объекта mike"
        assert vlad_show_contact in task_2_output, "Обратитесь к методу show_contact() объекта vlad"

