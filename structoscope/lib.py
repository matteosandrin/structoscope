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
        indices = '\n'.join(['<TD>{}</TD>'.format(i) for i in range(len(data))])
        values = '\n'.join(['<TD>{}</TD>'.format(v) for v in data])
        nodeLabel = nodeLabelTemplate.format(indices, values)

        graph.node('node0', nodeLabel)
        graph.edges([])
        graph.view()