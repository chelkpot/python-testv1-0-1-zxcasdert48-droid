import pytest
from unittest.mock import patch
from io import StringIO
import tasks.task4 as task4

def test_task4_celsius_to_fahrenheit(capsys):
    with patch('sys.stdin', StringIO('20\n')):
        exec(open('tasks/task4.py').read())
        captured = capsys.readouterr()
        assert "68.0" in captured.out