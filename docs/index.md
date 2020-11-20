Structoscope
============

Welcome to the documentation for the `structoscope` Python library!  
  
Structoscope is a Python library for visualizing and inspecting any data structure.

```eval_rst
.. toctree::
   :maxdepth: 2
   :caption: Reference

   structoscope
```

## Install

The only external dependency is the `graphviz` binary, which you can install buy running the following command in the terminal.  

```
$> brew install graphviz
```

Now you can install structoscope by running the following command in the terminal.

```
$> pip3 install structoscope
```

## Examples

Structoscope can easily display Python lists:

#### Input
```python
from structoscope import Scope

s = Scope("Test list")
testList = [1,2,3]
s.printList(testList)
```

#### Output
![Example 1](https://github.com/matteosandrin/structoscope/raw/master/example_01.png)

It can even display multi-dimensional lists:

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
![Example 2](https://github.com/matteosandrin/structoscope/raw/master/example_02.png)
