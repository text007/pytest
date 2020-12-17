
import pytest
import tasks
from tasks import Task


def test_add_returns_valid_id(tasks_db):
    """tasks.add(<valid task>) 应该返回一个整数。"""
    # 给定一个初始化的任务数据库
    # 当添加新任务时
    # 然后返回 task_id 为 int 类型
    new_task = Task("do something")
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)


def test_add_increases_count(db_with_3_tasks):
    """add()对task .count()的影响"""
    # 给定一个有3个任务的db
    # 当添加另一个任务时
    tasks.add(Task("Throw a party"))
    # 然后 count 增加1
    assert tasks.count() == 4
