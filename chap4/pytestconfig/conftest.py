

def pytest_addoption(parser):
    parser.addoption("--myopt", action="store_true",
                     help="som boolean option")
    parser.addoption("--foo", action="store", default="bar",
                     help="foo:bar or baz")
