pytest-nice: A pytest plugin
============================
Makes pytest output just a bit nic nicer during failures

Features
--------
- Includes user name of person running test in pytest output.
- Adds ''--nice'' option that:
    - turns ''f'' to ''o''
    - with ''-v'', turns ''FAILURE'' to ''OPPORTUNITY for improvement''
Installation
------------
Given that our pytest plugins are being saved in .tar.gz form in the shared directory PATH, then install like this:
::
    $ pip install PATH/pytest-nice-0.1.0.tar.gz
    $ pip install --no-index --find-links PATH pytest-nice
Usage
-----
::
    $ pytest -nice
