# tests/test_task2.py

import pytest
from unittest.mock import patch
from io import StringIO
from tasks.task2 import solve  # Теперь импортируем solve() напрямую

def test_task2_triangle_area(capsys):
    with patch('builtins.input', side_effect=['10', '5']):
        solve()
        captured = capsys.readouterr()
        assert "25.0" in captured.out