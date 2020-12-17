# 内置 Fixtue


# 使用 tmpdir 和 tmpdir_factory
"""
内置的 tmpdir 和 tmpdir_factory 负责在测试开始运行前创建临时文件目录,并在测试结束后删除.
单个测试使用 tmpdir,多个测试使用 tmpdir_factory。
tmpdir 的作用范围是函数级别, tmpdir-factory 的作用范围是会话级别

创建文件：tmpdir.join("something.txt")
        tmpdir_factory.join("something.txt")

创建目录：tmpdir.mkdir("anything")
        tmpdir_factory.mktemp("mydir")

read():读取文件内容
write():写入指定字符串
tmpdir_factory.getbasetemp()：目录路径

json.dump():将 Python 的字典结构写于到 json文件
json.load():将 json 读成 Python 的字典结构

open("w")：打开一个文件
r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
r+	打开一个文件用于读写。文件指针将会放在文件的开头。
rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。

"""


# 使用 pytestconfig
"""
设置添加命令行快捷方式
test_config.py
"""


# 使用 cache
"""
从一段测试会话传递信息给下一段会话。
test_slower.py
"""


# 使用 capsys
"""
允许使用代码读取stdout和stderr;
可以临时禁止抓取日志输出。

test_capsys.py
"""


# 使用 monkeypatch
"""
monkey patch可以在运行期间对类或模块进行动态修改。

setattr(target, name, value=(notset>, raising=True):设置一个属性。
delattr(target,name=<notset>, raising=True):删除一个属性。
setitem(dic, name, value):设置字典中的一条记录。
delitem(dic,name, raising=True):删除字典中的一条记录。
setenv (name, value, prepend=None):设置一个环境变量。
delenv (name, raising=True):删除一个环境变量。
syspath_prepend(path):将路径path加入sys.path并放在最前,sys.path是Python导入的系统路径列表。
chdir(path):改变当前的工作目录。


raising参数用于指示pytest是否在记录不存在时抛出异常。
test_cheese.py
"""


# 使用 doctest-namespace
"""
可以在函数的文档字符串中放入示例代码,并通过测试确保有效

unnecessary_math.py
"""


# 使用 recwarn
"""
内置的 recwarn 可以用来检查待测代码产生的警告信息。

"""