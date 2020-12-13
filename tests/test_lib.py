from structoscope import Scope
import pytest
import os.path


def test_Scope_getLabelForList_empty():
    s = Scope()
    assert s._getLabelForList([]) == '''<
<TABLE ALIGN="CENTER"
       BORDER="0"
       CELLBORDER="1"
       CELLSPACING="0"
       CELLPADDING="4">
<TR>
<TD COLSPAN="1">
<B>list</B><BR/>
<FONT POINT-SIZE="8">length: 0</FONT>
</TD>
    </TR>
    <TR>
<TD><FONT POINT-SIZE="8"> </FONT></TD>
    </TR>
    <TR>
<TD PORT="0"> </TD>
    </TR>
</TABLE>
>'''


def test_Scope_getLabelForList_withInts():
    s = Scope()
    assert s._getLabelForList([1, 2, 3]) == '''<
<TABLE ALIGN="CENTER"
       BORDER="0"
       CELLBORDER="1"
       CELLSPACING="0"
       CELLPADDING="4">
<TR>
<TD COLSPAN="3">
<B>list</B><BR/>
<FONT POINT-SIZE="8">length: 3</FONT>
</TD>
    </TR>
    <TR>
<TD><FONT POINT-SIZE="8">[0]</FONT></TD>
<TD><FONT POINT-SIZE="8">[1]</FONT></TD>
<TD><FONT POINT-SIZE="8">[2]</FONT></TD>
    </TR>
    <TR>
<TD PORT="0">1</TD>
<TD PORT="1">2</TD>
<TD PORT="2">3</TD>
    </TR>
</TABLE>
>'''


def test_Scope_getLabelForList_withStrings():
    s = Scope()
    assert s._getLabelForList(['a', 'b', 'c']) == '''<
<TABLE ALIGN="CENTER"
       BORDER="0"
       CELLBORDER="1"
       CELLSPACING="0"
       CELLPADDING="4">
<TR>
<TD COLSPAN="3">
<B>list</B><BR/>
<FONT POINT-SIZE="8">length: 3</FONT>
</TD>
    </TR>
    <TR>
<TD><FONT POINT-SIZE="8">[0]</FONT></TD>
<TD><FONT POINT-SIZE="8">[1]</FONT></TD>
<TD><FONT POINT-SIZE="8">[2]</FONT></TD>
    </TR>
    <TR>
<TD PORT="0">"a"</TD>
<TD PORT="1">"b"</TD>
<TD PORT="2">"c"</TD>
    </TR>
</TABLE>
>'''


def test_Scope_getLabelForDict():
    s = Scope()
    assert s._getLabelForDict({
        'a': 1,
        'b': 2,
        'c': 3,
    }) == '''<
<TABLE ALIGN="CENTER"
       BORDER="0"
       CELLBORDER="1"
       CELLSPACING="0"
       CELLPADDING="4">
<TR>
<TD COLSPAN="2">
<B>dict</B><BR/>
<FONT POINT-SIZE="8">length: 3</FONT>
</TD>
</TR>
<TR>
    <TD><B>key</B></TD>
    <TD><B>value</B></TD>
</TR>
<TR><TD>"a"</TD><TD>1</TD></TR>
<TR><TD>"b"</TD><TD>2</TD></TR>
<TR><TD>"c"</TD><TD>3</TD></TR>
</TABLE>
>'''


def test_Scope_printList_withWrongType():
    s = Scope()
    with pytest.raises(ValueError) as e:
        s.printList('test')
    assert str(e.value) == 'invalid argument type: <class \'str\'>'


def test_Scope_printList_withNestedArray():
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
    assert str(s.printList(testList, raw=True)) == result


def test_Scope_printDict_withWrongType():
    s = Scope()
    with pytest.raises(ValueError) as e:
        s.printDict('test')
    assert str(e.value) == 'invalid argument type: <class \'str\'>'


def test_Scope_printList_withSimpleDict():
    s = Scope()
    testDict = {
        'a': 1,
        'b': 2,
        'c': 3,
    }
    head, _ = os.path.split(__file__)
    result = open(os.path.join(head, 'data/printDictSimple.dot')).read()
    assert str(s.printDict(testDict, raw=True)) == result


def test_Scope_printList_withTree():

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
    assert str(s.printTree(root, raw=True)) == result


def test_Scope_toStr_withint():
    s = Scope()
    assert s._toStr(0) == '0'
    assert s._toStr(1) == '1'
    assert s._toStr(123) == '123'
    assert s._toStr(-123) == '-123'


def test_Scope_toStr_withstring():
    s = Scope()
    assert s._toStr('a') == '"a"'
    assert s._toStr('abc') == '"abc"'
    assert s._toStr('Hello World') == '"Hello World"'
    assert s._toStr('') == '""'
