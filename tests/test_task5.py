import pytest
from unittest.mock import patch
from io import StringIO
import tasks.task5 as task5

def test_task5_squares(capsys):
    with patch('sys.stdin', StringIO('2 3 4\n')):
        exec(open('tasks/task5.py').read())
        captured = capsys.readouterr()
        assert "4 9 16" in captured.out