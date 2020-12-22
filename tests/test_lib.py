from structoscope import Scope
import os.path


def test_Scope_print_withNestedArray():
    s = Scope()
    testList = [
        [1, 2],
        [
            ['a', 'b'],
            ['c', 'd']
        ],
        'abc'
    ]
    head, _ = os.path.split(__file__)
    result = open(os.path.join(head, 'data/printListNested.dot')).read()
    assert str(s.print(testList, raw=True)) == result


def test_Scope_print_withSimpleDict():
    s = Scope()
    testDict = {
        'a': 1,
        'b': 2,
        'c': 3,
    }
    head, _ = os.path.split(__file__)
    result = open(os.path.join(head, 'data/printDictSimple.dot')).read()
    assert str(s.print(testDict, raw=True)) == result


def test_Scope_print_withTree():

    class Node:
        def __init__(self, val=None, children=[]):
            self.val = val
            self.children = children

    s = Scope(
        dataMemberName='val',
        childrenMemberName='children'
    )
    node9 = Node(val='J')
    node8 = Node(val='I')
    node7 = Node(val='H')
    node6 = Node(val='G')
    node5 = Node(val='F')
    node4 = Node(val='E')
    node3 = Node(val='D', children=[node8, node9])
    node2 = Node(val='C', children=[node6, node7])
    node1 = Node(val='B', children=[node4, node5])
    root = Node(val='A', children=[node1, node2, node3])
    head, _ = os.path.split(__file__)
    result = open(os.path.join(head, 'data/printTree.dot')).read()
    assert str(s.print(root, raw=True)) == result
