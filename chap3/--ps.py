# pytest Fixture


# Fixture
"""
fixture是在测试函数运行前后,由pytest执行的外壳函数。

例：@pytest.fixture()
test_fixture.py
"""


# 通过 conftest.py 共享 fixture
"""
目录创建：目录和子目录可使用。
文件创建：该文件可使用。
"""


# 使用 fixture 执行配置及销毁逻辑
"""
cd a/tasks_proj/tests/conftest.py tasks_db()
"""


# 使用--setup-show回溯fixture的执行过程
"""
pytest --setup-show test_add.py -k valid_id
"""


# 指定 fixture 作用范围
"""
@pytest.fixture(scope="")

scope='function'
函数级别的 fixture 每个测试函数只需要运行一次。

scope='class'
类级别的 fixture 每个测试类只需要运行一次.

scope='module'
模块级别的 fixture 每个模块只需要运行一次.

scope='session'
会话级别的 fixture 每次会话只需要运行一次。

可以使用 --setup-show 命令行选项观察每个 fixture 被调用的次数,
以及在,各自作用范围下执行配置、销毁逻辑的顺序。
pytest --setup-show test_scope.py
"""


# 为常用的 fixture 添加 autouse 选项
"""
我们可以通过指定 autouse-True 选项,使作用域内的测试函数都运行该 fixture.

@pytest.fixture(autouse=True, scope="session")
"""


# 为 fixture 重命名
"""
@pytest.fixture(name="lue")
"""


# fixture 的参数化
"""
@pytest.fixture(params=tasks_to_try)
"""
