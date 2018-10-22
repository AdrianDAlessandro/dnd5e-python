# dnd5e-python

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/AdrianDAlessandro/dnd5e-python/master?filepath=character_scripting.ipynb)

A repository of a python-based interactive character sheet for Dungeons & Dragons 5th Edition.

Currently a jupyter notebook for scripting ideas and a module with some unit tests.

Using `pytest` for the unit tests, there is a `Dockerfile` that can be used to run the tests in a docker container.

To build the docker image, from the directory containing the Dockerfile, run:

```bash
docker build -t dnd5e-test .
```

Then start the container to run the unit tests with:

```bash
docker run -v `pwd`:/usr/src/app dnd5e-test
```

If you do not have Docker, run the tests in your prefered virtual environment, or base environment if you have pytest installed, with the command:

```bash
py.test
```

