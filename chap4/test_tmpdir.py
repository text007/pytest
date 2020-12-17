
def test_tmpdir(tmpdir):
    # tmpdir 已经有一个与之关联的路径名
    # join() 扩展路径以包含文件名
    # 创建文件
    a_file = tmpdir.join("something.txt")

    # 创建目录
    a_sub_dir = tmpdir.mkdir("anything")

    # 创建文件
    anothe_file = a_sub_dir.join("something_else.txt")

    # 写入"something.txt"
    a_file.write("contents may settle during shipping")

    # 写入"anything/something_else.txt"
    anothe_file.write("something different")

    # 读取文件进行比较
    assert a_file.read() == "contents may settle during shipping"
    assert anothe_file.read() == "something different"


def test_tmpdir_factory(tmpdir_factory):
    # 创建目录
    a_dir = tmpdir_factory.mktemp("mydir")

    # 目录路径
    base_tenp = tmpdir_factory.getbasetemp()
    print("base:", base_tenp)

    a_file = a_dir.join("something.txt")
    a_sub_dir = a_dir.mkdir("anything")
    another_file = a_sub_dir.join("something_else.txt")

    a_file.write("contents may settle during shipping")
    another_file.write("something different")
    assert a_file.read() == "contents may settle during shipping"
    assert another_file.read() == "something different"
