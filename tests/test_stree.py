from structoscope import Tree


class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children


def test_Tree_getLabelForTree():

    s = Tree({
        'children': 'children',
        'data': 'val'
    })

    root = Node(val=0, children=[
        Node(val=1),
        Node(val=2),
        Node(val=3)
    ])

    assert s._getLabelForNode(root) == '''<
<TABLE ALIGN="CENTER"
       BORDER="0"
       CELLBORDER="1"
       CELLSPACING="0"
       CELLPADDING="4">
<TR>
<TD COLSPAN="3">
<B>node</B><BR/>
<FONT POINT-SIZE="8">children: 3</FONT>
</TD>
</TR>
<TR>
<TD COLSPAN="3">0</TD>
</TR>
<TR>
<TD PORT="0"> </TD><TD PORT="1"> </TD><TD PORT="2"> </TD>
</TR>
</TABLE>
>'''


def test_Tree_findChildren():

    s = Tree({
        'children': 'children',
        'data': 'val'
    })
    node1 = Node(val=1, children=[]),
    node2 = Node(val=2, children=[]),
    node3 = Node(val=3, children=[])

    root = Node(val=0, children=[
        node1,
        node2,
        node3
    ])

    assert s._findChildren(root) == [root, node1, node2, node3]
