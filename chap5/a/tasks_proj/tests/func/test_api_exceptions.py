import pytest
import tasks
from tasks import Task

@pytest.mark.usefixtures("tasks_db")
class TestAdd():
    """"""

    def test_missing_summary(self):
        """如果摘要缺失，应引发异常。"""
        with pytest.raises(ValueError):
            tasks.add(Task(owner="bob"))

    def test_done_not_bool(self):
        """如果done不是一个bool，应该引发一个异常。"""
        with pytest.raises(ValueError):
            tasks.add(Task(summary="summary", done="True"))
