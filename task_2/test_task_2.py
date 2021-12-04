import pytest
try:
    import author
except ImportError:
    assert False, 'Не найден класс Contact'


class TestClassVariable:
    init_records = [{'name': "Test", 'phone': '123', "birthday": "03.12.2021", "address": "Moscow"}]

    @pytest.mark.parametrize("kwargs", init_records)
    def test_class_name(self, kwargs):
        assert hasattr(author, "Contact")
        result = author.Contact(**kwargs)
        assert hasattr(result, "name")
        assert hasattr(result, "phone")
        assert hasattr(result, "birthday")
        assert hasattr(result, "address")
