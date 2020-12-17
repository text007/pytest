
import sys

def greeting(name):
    print("Hi, {}".format(name))


def test_greeting(capsys):
    greeting("Earthing")
    out, err = capsys.readouterr()
    assert out == "Hi, Earthing\n"
    assert err == ""

    greeting("Brian")
    greeting("Nerd")
    out, err = capsys.readouterr()
    assert out == "Hi, Brian"
    assert err == ""


def yikes(problem):
    print("Yikes! {}".format(problem), file=sys.stderr)


def test_yikes(capsys):
    yikes("Out of coffee!")
    out, err = capsys.readouterr()
    assert out == ""
    assert "Out of coffee!" in err


def test_capsys_disabled(capsys):
    with capsys.disabled():
        print("\nalways print this")
    print("normal print, usually captured")
