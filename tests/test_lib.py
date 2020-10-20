from structoscope import Scope


def test_Scope_getLabelForList_empty():
    s = Scope()
    assert s._getLabelForList([], 'TestList') == '''<
<TABLE ALIGN="CENTER"
       BORDER="0"
       CELLBORDER="1"
       CELLSPACING="0"
       CELLPADDING="4">
    <TR>
<TD COLSPAN="0"><B>TestList</B></TD>
    </TR>
    <TR>

    </TR>
    <TR>

    </TR>
</TABLE>
>'''


def test_Scope_getLabelForList_withints():
    s = Scope()
    assert s._getLabelForList([1, 2, 3], 'TestList') == '''<
<TABLE ALIGN="CENTER"
       BORDER="0"
       CELLBORDER="1"
       CELLSPACING="0"
       CELLPADDING="4">
    <TR>
<TD COLSPAN="3"><B>TestList</B></TD>
    </TR>
    <TR>
<TD>0</TD><TD>1</TD><TD>2</TD>
    </TR>
    <TR>
<TD>1</TD><TD>2</TD><TD>3</TD>
    </TR>
</TABLE>
>'''


def test_Scope_getLabelForList_withstrings():
    s = Scope()
    assert s._getLabelForList(['a', 'b', 'c'], 'TestList') == '''<
<TABLE ALIGN="CENTER"
       BORDER="0"
       CELLBORDER="1"
       CELLSPACING="0"
       CELLPADDING="4">
    <TR>
<TD COLSPAN="3"><B>TestList</B></TD>
    </TR>
    <TR>
<TD>0</TD><TD>1</TD><TD>2</TD>
    </TR>
    <TR>
<TD>"a"</TD><TD>"b"</TD><TD>"c"</TD>
    </TR>
</TABLE>
>'''


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
