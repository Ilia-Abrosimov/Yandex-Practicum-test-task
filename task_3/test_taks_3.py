from task_3.author import long_heavy as author_long_heavy
from task_3.precode import long_heavy


class TestTask:

    def test_func_exist(self):
        try:
            from task_3 import precode
        except ImportError:
            assert False, 'Не найден модуль precode'
        assert hasattr(precode, "time_check"), "Не найден метод time_check"
        assert hasattr(precode, "long_heavy"), "Не найден метод long_heavy"
        assert hasattr(precode, "cache_args"), "Не найден метод cache_args"

    def test_long_heavy(self):
        author_result = author_long_heavy(3)
        precode_result = long_heavy(3)
        assert author_result == precode_result, "Не изменяйте функцию long_heavy"

    def test_output(self, task_3_output):
        one_sec_time = "Время выполнения функции: 1.0 с."
        zero_sec_time = "Время выполнения функции: 0.0 с."
        output = task_3_output.split("\n")
        author_result1 = author_long_heavy(1)
        author_result2 = author_long_heavy(2)
        try:
            assert one_sec_time == output[0], "Не изменяйте функцию time_check"
            assert str(author_result1) == output[1], "Неверный вывод функции long_heavy"
            assert zero_sec_time == output[2], "Декоратор cache_args не кеширует значение декорируемой функции"
            assert str(author_result1) == output[3], "Неверный вывод функции long_heavy"
            assert one_sec_time == output[4], "Не изменяйте функцию time_check"
            assert str(author_result2) == output[5], "Неверный вывод функции long_heavy"
            assert zero_sec_time == output[6], "Декоратор cache_args не кеширует значение декорируемой функции"
            assert str(author_result2) == output[7], "Неверный вывод функции long_heavy"
            assert zero_sec_time == output[8], "Декоратор cache_args не кеширует значение декорируемой функции"
            assert str(author_result2) == output[9], "Неверный вывод функции long_heavy"
        except IndexError:
            assert False, "Проверьте правильность вывода"
