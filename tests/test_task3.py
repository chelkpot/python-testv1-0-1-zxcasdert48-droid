import pytest
from unittest.mock import patch
from io import StringIO
import os

# Проверяем, существует ли файл с решением для Задания 3. Если нет, тест будет пропущен.
@pytest.mark.skipif(not os.path.exists("tasks/task3.py"), reason="File tasks/task3.py does not exist")
def test_task3_bmi(capsys):
    # Импортируем решение из файла задачи
    from tasks.task3 import solve
    with patch('builtins.input', side_effect=['70', '1.75']):
        solve()
        captured = capsys.readouterr()
        # Проверяем, что вывод содержит ожидаемый результат BMI
        assert "22.857142857142858" in captured.out