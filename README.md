# dnd5e-python

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/AdrianDAlessandro/dnd5e-python/master?filepath=character_scripting.ipynb)

A repository of a python-based interactive character sheet for Dungeons & Dragons 5th Edition.

Currently a jupyter notebook for scripting ideas and a module with some unit tests.

Using `pytest` for the unit tests, there is a `Dockerfile` that can be used to run the tests in a docker container.

If you do not have Docker, run the tests in your prefered virtual environment, or base environment if you have pytest installed, with the command:

```bash
py.test
```

