import pytest
from unittest.mock import patch
from io import StringIO
import tasks.task3 as task3

def test_task3_bmi(capsys):
    with patch('sys.stdin', StringIO('70\n1.75\n')):
        exec(open('tasks/task3.py').read())
        captured = capsys.readouterr()
        assert "22.857142857142858" in captured.out