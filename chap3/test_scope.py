
import pytest


@pytest.fixture(scope="function")
def func_scope():
    """一个函数范围 fixture"""


@pytest.fixture(scope="module")
def mod_scope():
    """一个模块范围 fixture"""


@pytest.fixture(scope="session")
def sess_scope():
    """一个会话范围 fixture"""


@pytest.fixture(scope="class")
def class_scope():
    """一个类范围 fixture"""


def test_1(sess_scope, mod_scope, func_scope):
    """使用会话、模块和函数范围 fixture 进行测试。"""


def test_2(sess_scope, mod_scope, func_scope):
    """使用多个测试演示更有趣。"""


@pytest.mark.usefixtures("class_scope")
class TestSomething():
    """演示类范围 fixture，"""
    def test_3(self):
        """使用类范围 fixture 进行测试。"""
    def test_4(self):
        """同样，多重测试更有趣。"""
