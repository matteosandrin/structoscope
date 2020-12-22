
GENERAL_TEMPLATE = '''<
<TABLE ALIGN="CENTER"
       BORDER="0"
       CELLBORDER="1"
       CELLSPACING="0"
       CELLPADDING="4">
{}
</TABLE>
>'''

LIST_TEMPLATE = GENERAL_TEMPLATE.format('''<TR>
<TD COLSPAN="{}">
<B>list</B><BR/>
<FONT POINT-SIZE="8">length: {}</FONT>
</TD>
    </TR>
    <TR>
{}
    </TR>
    <TR>
{}
    </TR>''')

DICT_TEMPLATE = GENERAL_TEMPLATE.format('''<TR>
<TD COLSPAN="2">
<B>dict</B><BR/>
<FONT POINT-SIZE="8">length: {}</FONT>
</TD>
</TR>
<TR>
    <TD><B>key</B></TD>
    <TD><B>value</B></TD>
</TR>
{}''')

NODE_TEMPLATE = GENERAL_TEMPLATE.format('''<TR>
<TD COLSPAN="{}">
<B>node</B><BR/>
<FONT POINT-SIZE="8">children: {}</FONT>
</TD>
</TR>
<TR>
<TD COLSPAN="{}">{}</TD>
</TR>
<TR>
{}
</TR>''')
