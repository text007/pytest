
import pytest
import tasks
from tasks import Task


def test_add_1():
    """tasks.get() 使用从 add() 返回的 id 可以工作。"""
    task = Task("breathe", "BRIAN", True)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    # 除了id之外，其他都应该一样
    assert equivalent(t_from_db, task)


def equivalent(t1, t2):
    """检查两个任务是否等价。"""
    # 比较除了id字段之外的所有内容
    return ((t1.summary == t2.summary) and
            (t1.owner == t2.owner) and
            (t1.done == t2.done))


@pytest.mark.parametrize("task",
                         [Task("sleep", done=True),
                          Task("wake", "brian"),
                          Task("sleep", "BRIAN", True),
                          Task("sleep", "BrIaN", False)])
def test_add_2(task):
    """演示用一个参数进行参数化。"""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    # 除了id之外，其他都应该一样
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize("summary, owner, done",
                         [("sleep", None, False),
                          ("wake", "brian", False),
                          ("sleep", "BRIAN", True),
                          ("eat eggs", "BrIaN", False)])
def test_add_3(summary, owner, done):
    """演示用一个参数进行参数化。"""
    task = Task(summary, owner, done)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    # 除了id之外，其他都应该一样
    assert equivalent(t_from_db, task)


tasks_to_try = (Task("sleep", done=True),
                Task("wake", "brian"),
                Task("sleep", "BRIAN", True),
                Task("exercise", "BrIaN", False))


@pytest.mark.parametrize("task", tasks_to_try)
def test_add_4(task):
    """演示用一个参数进行参数化。"""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    # 除了id之外，其他都应该一样
    assert equivalent(t_from_db, task)


task_ids = ["Task({},{},{})".format(t.summary, t.owner, t.done)
            for t in tasks_to_try]


@pytest.mark.parametrize("task", tasks_to_try, ids=task_ids)
def test_add_5(task):
    """演示用一个参数进行参数化。"""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    # 除了id之外，其他都应该一样
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize("task", tasks_to_try, ids=task_ids)
class TestAdd():

    def test_equivalent(self, task):
        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        assert equivalent(t_from_db, task)

    def test_valid_id(self, task):
        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        assert t_from_db.id == task_id


@pytest.mark.parametrize("task", [
    pytest.param(Task("create"), id="just summary"),
    pytest.param(Task("inspire", "Michelle"), id="summary/owner"),
    pytest.param(Task("encourage", "Michelle", True), id="summary/owner/done")])
def test_add_6(task):
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """在测试前连接数据库，断开连接。"""
    # 设置:启动数据库
    tasks.start_tasks_db(str(tmpdir), "tiny")

    yield   # 这是测试发生的地方

    # 拆卸:停止数据库
    tasks.stop_tasks_db()