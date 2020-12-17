
import pytest
import tasks
from tasks import Task

# 提醒任务构造函数接口
# Task(summary=None, owner=None, done=False, id-None)
# 总结是必需的
# owner和done是可选的
# id由数据库设置
@pytest.fixture(scope="session")
def tasks_just_a_few():
    """所有摘要和所有者是唯一的。"""
    return (Task("Write some code", "Brian", True),
            Task("Code review Brian's code", "Katie", False),
            Task("Fix what Brian did", "Michelle", False))

@pytest.fixture(scope="session")
def tasks_mult_per_owner():
    """几个所有者，每个所有者有几个任务。"""
    return (
        Task("Make a cookie", "Raphael"),
        Task("Use an emoji", "Raphael"),
        Task("Move to Berlin", "Raphael"),

        Task("Create", "Michelle"),
        Task("Inspire", "Michelle"),
        Task("Encourage", "Michelle"),

        Task("Do a handstand", "Daniel"),
        Task("Write some books", "Daniel"),
        Task("Eat ice cream", "Daniel"))


@pytest.fixture()
def db_with_3_tasks(tasks_db, tasks_just_a_few):
    """连接的db有3个任务，都是唯一的，"""
    for t in tasks_just_a_few:
        tasks.add(t)


@pytest.fixture()
def db_with_multi_per_owner(tasks_db, tasks_mult_per_owner):
    """连接的db有9个任务，3个所有者，都有3个任务。"""
    for t in tasks_mult_per_owner:
        tasks.add(t)


@pytest.fixture(scope="session", params=["tiny", "mongo"])
def tasks_db_session(tmpdir_factory, request):
    """在测试前连接数据库，断开连接。"""
    # 设置:启动数据库
    temp_dir = tmpdir_factory.mktemp("temp")
    tasks.start_tasks_db(str(temp_dir), request.param)

    yield   # 这是测试发生的地方

    # 拆卸:停止数据库
    tasks.stop_tasks_db()


@pytest.fixture()
def tasks_db(tasks_db_session):
    tasks.delete_all()


def pytest_report_heaber():
    """"""
    return "Thanks for running the tests."


def pytest_report_teststatus(report):
    if report.when == "call" and report.failed:
        return (report.outcome, "O", "OPPORTUNITY for improvement")
