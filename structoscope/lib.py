from graphviz import Digraph
import os


def echo(arg):
    return arg


class Scope:

    def printList(self, data, name):
        if not isinstance(data, list):
            raise ValueError('invalid argument type: {}'.format(type(data)))

        tempFolder = os.environ['TMPDIR']

        graph = Digraph('list_graph',
                        directory=tempFolder,
                        node_attr={'shape': 'none'})
        graph.node('node0', self._getLabelForList(data, name))
        graph.edges([])
        graph.view()

    def _getLabelForList(self, data, name):
        nodeLabelTemplate = '''<
<TABLE ALIGN="CENTER"
       BORDER="0"
       CELLBORDER="1"
       CELLSPACING="0"
       CELLPADDING="4">
    <TR>
<TD COLSPAN="{}"><B>{}</B></TD>
    </TR>
    <TR>
{}
    </TR>
    <TR>
{}
    </TR>
</TABLE>
>'''
        cellTemp = '<TD>{}</TD>'
        indices = [cellTemp.format(self._toStr(i)) for i in range(len(data))]
        indices = ''.join(indices)
        values = [cellTemp.format(self._toStr(v)) for v in data]
        values = ''.join(values)
        return nodeLabelTemplate.format(len(data), name, indices, values)

    def _toStr(self, value):
        if isinstance(value, str):
            return '"{}"'.format(value)
        return str(value)
