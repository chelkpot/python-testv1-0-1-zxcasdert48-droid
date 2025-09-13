import pytest
from unittest.mock import patch
from io import StringIO
import tasks.task2 as task2

def test_task2_triangle_area(capsys):
    with patch('sys.stdin', StringIO('10\n5\n')):
        exec(open('tasks/task2.py').read())
        captured = capsys.readouterr()
        assert "25.0" in captured.out