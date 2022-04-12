import pytest

@pytes.mark.parametrize("test_input", [1, 2, 3])
class TestClassParametrized:
    # Все функции должны использовать аргумент
    def test_one(self, test_input):
        pass
    def test_two(self, test_input):
        pass

    # Каждый тест прогоняется через эти параметры