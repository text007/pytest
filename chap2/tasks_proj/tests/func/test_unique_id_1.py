
import pytest
import tasks

def test_unique_id():
    """ 调用unique_id() 两次将返回不同的数字。"""
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2
