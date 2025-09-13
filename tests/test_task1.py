# tests/test_task1.py

import pytest
from unittest.mock import patch
from io import StringIO
# Импортируем функцию solve из файла task1
from tasks.task1 import solve

def test_task1_sum_numbers(capsys):
    # Мы имитируем ввод данных '3' и '7'
    with patch('builtins.input', side_effect=['3', '7']):
        solve()  # Теперь мы напрямую вызываем функцию solve()
        captured = capsys.readouterr()
        # Проверяем, что вывод содержит ожидаемую строку
        assert "Сумма: 10" in captured.out