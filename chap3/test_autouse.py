
import pytest
import time


@pytest.fixture(autouse=True, scope="session")
def footer_session_scope():
    """会话结束时打印测试日期"""
    yield
    now = time.time()
    print("--")
    print("finished:{}".format(time.strftime("%d %b %x", time.localtime(now))))
    print("----------")


@pytest.fixture(autouse=True)
def footer_function_scope():
    """每个函数运行完打印测试时间"""
    start = time.time()
    yield
    stop = time.time()
    delta = stop - start
    print("\ntest duration : {:0.3} seconds".format(delta))


def test_1():
    time.sleep(1)


def test_2():
    time.sleep(1.25)
