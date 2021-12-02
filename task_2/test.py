import pytest
from author import Contact


class TestClassVariable:
    def test_class_name(self, user_code_test_2):
        assert f"class {Contact.__name__}:" in user_code_test_2, "Нет класса Contact"
        assert "self.name= name" in user_code_test_2.replace(" ", ""), "У класса Contact отсутствует свойство 'name'"
        assert "self.phone = phone" in user_code_test_2, "У класса Contact отсутствует свойство 'phone'"
        assert "self.birthday = birthday" in user_code_test_2, "У класса Contact отсутствует свойство 'birthday'"
        assert "self.address = address" in user_code_test_2, "У класса Contact отсутствует свойство 'address'"
