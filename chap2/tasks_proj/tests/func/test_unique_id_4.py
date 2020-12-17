
import pytest
import tasks
from tasks import Task


@pytest.mark.xfail(tasks.__version__ < "0.2.0",
                    reason="not supported until version 0.2.0")
def test_unique_id_1():
    """ 调用unique_id() 两次将返回不同的数字。"""
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2


@pytest.mark.xfail()
def test_unique_id_is_a_duck():
    """演示 xfail"""
    uid = tasks.unique_id()
    assert uid == "a duck"


@pytest.mark.xfail()
def test_unique_id_not_a_duck():
    """演示 xpass"""
    uid = tasks.unique_id()
    assert uid != "a duck"


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """在测试前连接数据库，断开连接。"""
    # 设置:启动数据库
    tasks.start_tasks_db(str(tmpdir), "tiny")

    yield   # 这是测试发生的地方

    # 拆卸:停止数据库
    tasks.stop_tasks_db()
