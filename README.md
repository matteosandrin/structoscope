# Structoscope
![License](https://img.shields.io/github/license/matteosandrin/structoscope)
![Python Version](https://img.shields.io/badge/python-3.8-blue)
![Build](https://img.shields.io/github/workflow/status/matteosandrin/structoscope/test/master)
![Coverage](https://img.shields.io/codecov/c/github/matteosandrin/structoscope/master)
![GitHub last commit](https://img.shields.io/github/last-commit/matteosandrin/structoscope)
![Documentation Status](https://readthedocs.org/projects/structoscope/badge/?version=latest)


Structoscope is a Python library for visualizing and inspecting any data structure.

## Install

The only external dependency is the `graphviz` binary, which you can install buy running the following command in the terminal.  

```
brew install graphviz
```

Now you can install structoscope by running the following command in the terminal.

```
pip3 install structoscope
```

## Examples

Structoscope can easily display Python lists:

#### Input
```python
from structoscope import Scope

s = Scope()
testList = [1,2,3]
s.printList(testList)
```

#### Output
![Example 1](example_01.png)

It can even display multi-dimensional lists:

#### Input
```python
from structoscope import Scope

s = Scope()
testList = [
    [1,2],
    [
        ['a', 'b'],
        ['c', 'd']
    ],
    'abc'
]
s.printList(testList)
```

#### Output
![Example 2](example_02.png)

Or it can display dictionaries:

#### Input
```python
from structoscope import Scope

s = Scope()
testDict = {
    'first' : 101,
    'second' : 102,
    'third' : 103,
}
s.printDict(testDict)
```

#### Output
![Example 3](example_03.png)


## Documentation

You can find the documentation for this project [here](https://structoscope.readthedocs.io/en/latest/).

## What's up with the name?

I think of it as a *stethoscope* whose purpose is to inspect a `struct`. A Struct-o-scope!
