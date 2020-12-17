import copy
import cheeses


def test_def_prefs_full():
    cheeses.write_default_cheese_preferences()
    expected = cheeses._default_prefs
    actual = cheeses.read_cheese_preferences()
    assert expected == actual


def test_def_prefs_change_home(tmpdir, monkeypatch):
    monkeypatch.setenv('HOME', tmpdir.mkdir('home'))
    cheeses.write_default_cheese_preferences()
    expected = cheeses._default_prefs
    actual = cheeses.read_cheese_preferences()
    assert expected == actual


def test_def_prefs_change_expanduser(tmpdir, monkeypatch):
    fake_home_dir = tmpdir.mkdir('home')
    monkeypatch.setattr(cheeses.os.path, 'expanduser',
                        (lambda x: x.replace('~', str(fake_home_dir))))
    cheeses.write_default_cheese_preferences()
    expected = cheeses._default_prefs
    actual = cheeses.read_cheese_preferences()
    assert expected == actual


def test_def_prefs_change_defaults(tmpdir, monkeypatch):
    # write the file once
    fake_home_dir = tmpdir.mkdir('home')
    monkeypatch.setattr(cheeses.os.path, 'expanduser',
                        (lambda x: x.replace('~', str(fake_home_dir))))
    cheeses.write_default_cheese_preferences()
    defaults_before = copy.deepcopy(cheeses._default_prefs)

    # change the defaults
    monkeypatch.setitem(cheeses._default_prefs, 'slicing', ['provolone'])
    monkeypatch.setitem(cheeses._default_prefs, 'spreadable', ['brie'])
    monkeypatch.setitem(cheeses._default_prefs, 'salads', ['pepper jack'])
    defaults_modified = cheeses._default_prefs

    # write it again with modified defaults
    cheeses.write_default_cheese_preferences()

    # read, and check
    actual = cheeses.read_cheese_preferences()
    assert defaults_modified == actual
    assert defaults_modified != defaults_before
