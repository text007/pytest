
import pytest
import tasks
from tasks import Task

import pytest
import tasks
from tasks import Task

tasks_to_try = (Task("sleep", done=True),
                Task("wake", "brian"),
                Task("sleep", "BRIAN", True),
                Task("exercise", "BrIaN", False))

task_ids = ["Task({},{},{})".format(t.summary, t.owner, t.done)
            for t in tasks_to_try]


def equivalent(t1, t2):
    """检查两个任务是否等价。"""
    # 比较除了id字段之外的所有内容
    return ((t1.summary == t2.summary) and
            (t1.owner == t2.owner) and
            (t1.done == t2.done))


@pytest.fixture(params=tasks_to_try)
def a_task(request):
    return request.param


def test_add_a(tasks_db, a_task):
    """演示用一个参数进行参数化。"""
    task_id = tasks.add(a_task)
    t_from_db = tasks.get(task_id)
    # 除了id之外，其他都应该一样
    assert equivalent(t_from_db, a_task)


@pytest.fixture(params=tasks_to_try, ids=task_ids)
def b_task(request):
    return request.param


def test_add_b(tasks_db, b_task):
    """演示用一个参数进行参数化。"""
    task_id = tasks.add(b_task)
    t_from_db = tasks.get(task_id)
    # 除了id之外，其他都应该一样
    assert equivalent(t_from_db, b_task)


def id_func(fixture_value):
    t = fixture_value
    return "Task({},{},{})".format(t.summary, t.owner, t.done)


@pytest.fixture(params=tasks_to_try, ids=id_func)
def c_task(request):
    return request.param


def test_add_c(tasks_db, c_task):
    task_id = tasks.add(c_task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, c_task)
