# Structoscope
![License](https://img.shields.io/github/license/matteosandrin/structoscope)
![Python Version](https://img.shields.io/badge/python-3.8-blue)
![Build](https://img.shields.io/github/workflow/status/matteosandrin/structoscope/test/master)
![Coverage](https://img.shields.io/codecov/c/github/matteosandrin/structoscope/master)
![GitHub last commit](https://img.shields.io/github/last-commit/matteosandrin/structoscope)
![Documentation Status](https://readthedocs.org/projects/structoscope/badge/?version=latest)


Structoscope is a Python library for visualizing and inspecting any data structure.

### What's up with the name?

I think of it as a *stethoscope* whose purpose is to inspect a `struct`. A Struct-o-scope!

### Documentation

You can find the documentation for this project [here](https://structoscope.readthedocs.io/en/latest/).

### Quick Example

This is how you display a list:

#### Input
```python
from structoscope import Scope

s = Scope("Test list")
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
![Example 1](example_01.png)
