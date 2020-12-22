from structoscope import List
import pytest


def test_List_getLabelForList_empty():
    s = List()
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


def test_List_getLabelForList_withInts():
    s = List()
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


def test_List_getLabelForList_withStrings():
    s = List()
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
<TD PORT="0">'a'</TD>
<TD PORT="1">'b'</TD>
<TD PORT="2">'c'</TD>
    </TR>
</TABLE>
>'''


def test_List_makeGraph_withWrongType():
    s = List()
    with pytest.raises(ValueError) as e:
        s.makeGraph('test')
    assert str(e.value) == 'invalid argument type: <class \'str\'>'
