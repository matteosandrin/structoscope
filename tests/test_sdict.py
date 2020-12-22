from structoscope import Dict
import pytest


def test_Dict_getLabelForDict():
    s = Dict()
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
<TR><TD>'a'</TD><TD>1</TD></TR>
<TR><TD>'b'</TD><TD>2</TD></TR>
<TR><TD>'c'</TD><TD>3</TD></TR>
</TABLE>
>'''


def test_Dict_makeGraph_withWrongType():
    s = Dict()
    with pytest.raises(ValueError) as e:
        s.makeGraph('test')
    assert str(e.value) == 'invalid argument type: <class \'str\'>'
