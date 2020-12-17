
import pytest
import tasks
from tasks import Task


def test_add_returns_valid_id():
    """tasks.add(<valid task>) 应该返回一个整数。"""
    # 给定一个初始化的任务数据库
    # 当添加新任务时
    # 然后返回的task_id是int类型的
    new_task = Task("do something")
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)


@pytest.mark.smoke
def test_added_task_has_id_set():
    """确保 task_id 字段设置为 tasks.add()"""
    # 给定一个初始化的任务数据库
    # 并添加一个新任务
    new_task = Task("sit in chair", owner="me", done=True)
    task_id = tasks.add(new_task)

    # 当任务被检索时
    task_from_db = tasks.get(task_id)

    # 然后 task_id 匹配 id 字段
    assert task_from_db.id == task_id


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """在测试前连接数据库，断开连接。"""
    # 设置:启动数据库
    tasks.start_tasks_db(str(tmpdir), "tiny")

    yield   # 这是测试发生的地方

    # 拆卸:停止数据库
    tasks.stop_tasks_db()
