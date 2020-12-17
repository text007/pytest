
import json
import pytest


@pytest.fixture(scope="module")
def author_file_json(tmpdir_factory):

    python_author_data = {
        "Ned": {"City": "Boston"},
        "Brian": {"City": "Portland"},
        "Luciano": {"City": "Sau paulo"}}

    # 创建临时目录，创建临时文件
    file = tmpdir_factory.mktemp("data").join("author_file.json")
    print("file:{}".format(str(file)))

    # 写于json 文件中
    with file.open("w") as f:
        json.dump(python_author_data, f)
    return file
