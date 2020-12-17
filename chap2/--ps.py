# 编写测试函数


# 本地安装 Tasks 项目程序包
"""
安装测试项目
项目下载地址：https://pragprog.com/titles/bopytest/python-testing-with-pytest/
pip install .
pip install --no-cache-dir .

安装后希望修改源码重新安装,就需要使用-e选项(editable) 。
pip install -e .
"""


# 测试函数的标记
"""
pytest提供了标记机制,允许你使用marker对测试函数做标记。
一个测试函数可以有多个marker,一个marker也可以用来标记多个测试函数。

例：test_api_exceptions.py
   @pytest.mark.smoke
   :pytest -v -m "smoke and get" test_api_exceptions.py
"""


# 跳过测试
"""
pytest 自身内置了一些标记: skip、skipif、xfail
skip 和 skipif 允许你跳过不希望运行的测试，测试会直接跳过,而不会被执行。
xfail 则告诉 pytest 运行此测试,但我们预期它会失败。
      XFAIL:预期失败,实际上也失败了
      XPASS:预期失败,实际运行并没有失败

-rs:显示出跳过的理由
例：pytest -rs test_unique_id_3.py

skip
例：test_unique_id_2.py
@pytest.mark.skip(reason="misunderstood the api")

skipif
例：test_unique_id_3.py
@pytest.mark.skipif(tasks.__version__ < "0.2.0",
                    reason="not supported until version 0.2.0")

xfail
例：test_unique_id_4.py
@pytest.mark.xfail()
pytest -v test_unique_id_4.py
"""


# 参数化参数
"""
参数化测试允许传递多组数据,一旦发现测试失败, pytest会及时报告。
@pytest.mark.parametrize(argnames, argnames)
parametrize()的第一个参数是用逗号分隔的字符串列表,本例中只有一个'task';
    第二个参数是一个值列表,本例中是一个Task对象列表。
例：test_add_variety.py::test_add_2

可以使用完整的测试标识(pytest术语为node)来重新指定需要运行单个参数的测试。
例：test_add_variety.py::test_add_3
pytest -v "test_add_variety.py::test_add_3[eat eggs-BrIaN-False]"
如果标识中包含空格,别忘了添加引号。
"""
