import pytest
from unittest.mock import patch
from io import StringIO
import os

# Проверяем, существует ли файл с решением для Задания 5. Если нет, тест будет пропущен.
@pytest.mark.skipif(not os.path.exists("tasks/task5.py"), reason="File tasks/task5.py does not exist")
def test_task5_squares(capsys):
    # Импортируем решение из файла задачи
    from tasks.task5 import solve
    # Используем side_effect, чтобы передать несколько значений
    with patch('builtins.input', side_effect=['2 3 4']):
        solve()
        captured = capsys.readouterr()
        # Проверяем, что вывод содержит ожидаемую строку
        assert "4 9 16" in captured.out