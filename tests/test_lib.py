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
