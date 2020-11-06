from structoscope import Scope


def test_Scope_getLabelForList_empty():
    s = Scope('TestList')
    assert s._getLabelForList([]) == '''<
<TABLE ALIGN="CENTER"
       BORDER="0"
       CELLBORDER="1"
       CELLSPACING="0"
       CELLPADDING="4">
    <TR>
<TD COLSPAN="1">
<B>TestList</B><BR/>
<FONT POINT-SIZE="8">length: 0</FONT>
</TD>
    </TR>
    <TR>
<TD><FONT POINT-SIZE="8"> </FONT></TD>
    </TR>
    <TR>
<TD> </TD>
    </TR>
</TABLE>
>'''


def test_Scope_getLabelForList_withints():
    s = Scope('TestList')
    assert s._getLabelForList([1, 2, 3]) == '''<
<TABLE ALIGN="CENTER"
       BORDER="0"
       CELLBORDER="1"
       CELLSPACING="0"
       CELLPADDING="4">
    <TR>
<TD COLSPAN="3">
<B>TestList</B><BR/>
<FONT POINT-SIZE="8">length: 3</FONT>
</TD>
    </TR>
    <TR>
<TD><FONT POINT-SIZE="8">[0]</FONT></TD>
<TD><FONT POINT-SIZE="8">[1]</FONT></TD>
<TD><FONT POINT-SIZE="8">[2]</FONT></TD>
    </TR>
    <TR>
<TD>1</TD>
<TD>2</TD>
<TD>3</TD>
    </TR>
</TABLE>
>'''


def test_Scope_getLabelForList_withstrings():
    s = Scope('TestList')
    assert s._getLabelForList(['a', 'b', 'c']) == '''<
<TABLE ALIGN="CENTER"
       BORDER="0"
       CELLBORDER="1"
       CELLSPACING="0"
       CELLPADDING="4">
    <TR>
<TD COLSPAN="3">
<B>TestList</B><BR/>
<FONT POINT-SIZE="8">length: 3</FONT>
</TD>
    </TR>
    <TR>
<TD><FONT POINT-SIZE="8">[0]</FONT></TD>
<TD><FONT POINT-SIZE="8">[1]</FONT></TD>
<TD><FONT POINT-SIZE="8">[2]</FONT></TD>
    </TR>
    <TR>
<TD>"a"</TD>
<TD>"b"</TD>
<TD>"c"</TD>
    </TR>
</TABLE>
>'''


def test_Scope_toStr_withint():
    s = Scope("TestList")
    assert s._toStr(0) == '0'
    assert s._toStr(1) == '1'
    assert s._toStr(123) == '123'
    assert s._toStr(-123) == '-123'


def test_Scope_toStr_withstring():
    s = Scope("TestList")
    assert s._toStr('a') == '"a"'
    assert s._toStr('abc') == '"abc"'
    assert s._toStr('Hello World') == '"Hello World"'
    assert s._toStr('') == '""'
