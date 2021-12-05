from task_4.precode import make_divider_of
from task_4.author import make_divider_of as author_make_divider_of


class TestTask:

    def test_func_exist(self):
        try:
            from task_4 import precode
        except ImportError:
            assert False, 'Не найден модуль precode'
        assert hasattr(precode, "make_divider_of"), "Не удаляйте функцию make_divider_of"
        func = precode.make_divider_of(5)
        assert func.__name__ == "division_operation", "Не удаляйте функцию division_operation"

    def test_result(self):
        precode_func = make_divider_of(5)
        precode_result = precode_func(10)
        author_func = author_make_divider_of(5)
        author_result = author_func(10)
        assert precode_result == author_result, "Функция неправильно считает результат"
        assert type(precode_result) == type(author_result), "Тип данных функции make_divider_of должен быть float"

    def test_output(self, task_4_output):
        output = task_4_output.split("\n")
        div2 = author_make_divider_of(2)
        author_result_1 = div2(10)
        try:
            assert str(author_result_1) == output[0], "Проверьте правильность вывода функции div2(10)"
            div5 = author_make_divider_of(5)
            author_result_2 = div5(20)
            assert str(author_result_2) == output[1], "Проверьте правильность вывода функции div5(20)"
            final_result = div5(div2(20))
            assert str(final_result) == output[2], "Проверьте правильность вывода функции div5(div2(20)"
        except IndexError:
            assert False, "Проверьте правильность вывода"
