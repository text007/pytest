import pytest
import tasks
from tasks import Task

@pytest.mark.usefixtures("tasks_db")
class TestAdd():
    """"""

    def test_missing_summary(self):
        """"""
        with pytest.raises(ValueError):
            tasks.add(Task(owner="bob"))

    def test_done_not_bool(self):
        """"""
        with pytest.raises(ValueError):
            tasks.add(Task(summary="summary", done="True"))
