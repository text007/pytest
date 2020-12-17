# 演示 fixture 重命名。
import pytest


@pytest.fixture(name="lue")
def ultimate_answer_to_life_the_nuiverse_and_everything():
    return 42


def test_everything(lue):
    assert lue == 42
