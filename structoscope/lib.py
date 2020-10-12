from graphviz import Digraph
import os

def echo(arg):
    return arg

class Scope:

    def printList(self, data):
        if not isinstance(data, list):
            raise ValueError('invalid argument type: {}'.format(type(data)))

        tempFolder = os.environ['TMPDIR']

        graph = Digraph('list_graph', directory=tempFolder, node_attr={ 'shape' : 'none' })
        graph.node('node0', self._getLabelForList(data))
        graph.edges([])
        graph.view()

    def _getLabelForList(self, data):
        nodeLabelTemplate = '''<
        <TABLE ALIGN="CENTER" BORDER="1">
            <TR>
                {}
            </TR>
            <TR>
                {}
            </TR>
        </TABLE>
        >'''
        indices = ''.join(['<TD>{}</TD>'.format(self._toStr(i)) for i in range(len(data))])
        values = ''.join(['<TD>{}</TD>'.format(self._toStr(v)) for v in data])
        return nodeLabelTemplate.format(indices, values)

    def _toStr(self, value):
        if isinstance(value, str):
            return '"{}"'.format(value)
        return str(value)