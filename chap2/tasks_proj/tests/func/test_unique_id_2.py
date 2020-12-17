
import pytest
import tasks
from tasks import Task


@pytest.mark.skip(reason="misunderstood the api")
def test_unique_id_1():
    """ 调用unique_id() 两次将返回不同的数字。"""
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2


def test_unique_id_2():
    """unique_id() 应该返回一个未使用的 id。"""
    ids = []
    ids.append(tasks.add(Task("one")))
    ids.append(tasks.add(Task("two")))
    ids.append(tasks.add(Task("three")))
    # 获取唯一id
    uid = tasks.unique_id()
    # 确保它不在存储 ids 列表中
    assert uid not in ids


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """在测试前连接数据库，断开连接。"""
    # 设置:启动数据库
    tasks.start_tasks_db(str(tmpdir), "tiny")

    yield   # 这是测试发生的地方

    # 拆卸:停止数据库
    tasks.stop_tasks_db()
