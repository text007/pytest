# 第一章 pytest 入门


# 命令行输出 pytest test_ch1_1_1.py
"""
test one.py 后方的一个点号(.) 表示:运行了一个测试用例,且测试通过。
如果想查看详情,可以在 pytest 后面加上 -v 或者 --verbose选项。

例：pytest test_ch1_1_1.py
"""


# 测试结果显示
"""
PASSED(.):测试通过。
FAILED(F):测试失败(也有可能是XPASS状态与strict选项冲突造成的失败,见后文) 。
SKIPPED(s):测试未被执行。指定测试跳过执行,可以将测试标记为@pytest.mark.skip(),或者使用@pytest.mark.skipif()指定跳过测试的条件.
xfal(x):预期测试失败,并且确实失败。使用@pytest.mark. xfai()指定你认为会失败的测试用例.
XPASS(X):预期测试失败,但实际上运行通过,不符合预期。
ERROR(E):测试用例之外的代码触发了异常,可能由fixture引起,也可能由hook函数引起。
"""


# 使用命令行选项  pytest --help
# --collect-only 选项
"""
使用 --collect-only 选项可以展示在给定的配置下哪些测试用例会被运行。

例：pytest --collect-only
"""

# -k 选项
"""
-k选项允许你使用表达式指定希望运行的测试用例。

例：pytest -k "asdict or defaults" --collect-only
pytest -k "asdict or defaults"
"""

# -m 选项
"""
标记 (marker) 用于标记测试并分组,以便快速选中并运行.

使用 -m 选项可以用表达式指定多个标记名。
使用 -m"mark1 and mark2" 可以同时选中带有这两个标记的所有测试用例。
使用 -m"mark1 and not mark2"· 则会选中带有 mark1 的测试用例,而过滤掉带有 mark2 的测试用例;
使用 -m"mark1 or mark2" 则选中带有 mark1 或者 mark2 的所有测试用例。

例：tasks>pytest -v -m run_these_please
"""

# -x 选项
"""
-x选项遇到失败时会立即停止整个会话.

例：pytest -x
"""

# --maxfail=num 选项
"""
--maxfail=num 选项允许 pytest 失败几次后再停止,可以使用 --maxfail 选项,明确指定可以失败几次。

失败一次停止
例：pytest --maxfail=1
"""

# -s 与 --capture=method 选项
"""
-s选项允许终端在测试运行时输出某些结果,包括任何符合标准的输出流信息。-s 等价于 --capture=no.

例：pytest -s
"""

# --lf(--last-failed) 选项
"""
当一个或多个测试失败时,我们常常希望能够定位到最后一个失败的测试用例重新运行,这时可以使用--lf选项。

例：pytest --lf
"""

# --ff(--failed-first) 选项
"""
优先运行上次失败的用例，再运行完其他的用例。

例：pytest --ff --tb=no
"""

# -v(--verbose) 选项
"""
使用-v/-verbose选项,输出的信息会更详细。
最明显的区别就是每个文件中的每个测试用例都占一行(先前是每个文件占一行) ,测试的名字和结果都会显示出来,而不仅仅是一个点或字符.

例：pytest -v --ff --tb=no
"""

# -q(--quiet) 选项
"""
该选项的作用与-v/-verbose的相反,它会简化输出信息。
将-q和--tb-line (仅打印异常的代码位置)搭配使用。

例：pytest -q
"""

# -l(--showlocals) 选项
"""
使用-l选项,失败测试用例由于被堆栈追踪,所以局部变量及其值都会显示出来。

例：pytest -l tasks
"""

# --tb=style 选项
"""
--tb=tyle选项决定捕捉到失败时输出信息的显示方式。
推荐的 style 类型有 short, line, no.

short 模式仅输出 assert 的一行以及系统判定内容(不显示上下文).
例：pytest --tb=short tasks

line模式只使用一行输出显示所有的错误信息.
例：pytest --tb=line tasks

no模式则直接屏蔽全部回溯信息。
例：pytest --tb=no tasks

--tb=long输出最为详尽的回溯信息; 
--tb-auto是默认值,如果有多个测试用例失败,仅打印第一个和最后一个用例的回溯信息(格式与1ong模式的-致) ; 
--tb=native只输出Python标准库的回溯信息,不显示额外信息。
"""

# --duration=N 选项
"""
--duratio-N选项可以加快测试节奏。
它不关心测试是如何运行的,只统计测试过程中哪几个阶段是最慢的(包括每个测试用例的call, setup, teardown过程) 。
它会显示最慢的N个阶段,耗时越长越靠前。如果使用--duration=0,则会将所有阶段按耗时从长到短排序后显示。

例：pytest --durations=3 tasks
"""

# --version 选项
"""
使用--version可以显示当前的pytest版本

例：python --version
"""

# -h(--help) 选项
"""
能展示原生pytest的用法,还展示新添加的插件的选项和用法。

使用-h选项可以获得:
基本用法: pytest [options] [file-ordir] [fileor-dir] [...]
命令行选项及其用法,包括新添加的插件的选项及其用法。
可用于ini配置文件中的选项(第6章会详细介绍)。
影响pytest行为的环境变量(第6章会详细介绍)
使用pytest--markers时的可用marker列表(第2章会详细介绍).
使用pytest--fixtures时的可用fixture列表(第3章会详细介绍)。

例：pytest -h
"""
