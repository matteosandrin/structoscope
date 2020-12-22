from lib import GENERAL_TEMPLATE
from graphviz import Digraph
import os

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

class List:

    def printList(self, data, raw=False):
        """
        Creates a visualization of a Python list

        :param data: The list to visualize
        :type data: list
        """

        if not isinstance(data, list):
            raise ValueError('invalid argument type: {}'.format(type(data)))
        try:
            tempFolder = os.environ['TMPDIR']
        except Exception:
            tempFolder = "."
        graph = Digraph('list_graph',
                        directory=tempFolder,
                        node_attr={'shape': 'none'},
                        graph_attr={'dpi': '300'},
                        edge_attr={
                            'tailclip': 'false',
                            'dir': 'both',
                            'arrowtail': 'dot',
                            'arrowsize': '0.5'
                        })
        graph.format = 'svg'
        nestedLists = self._findNestedLists(data)
        for i, llist in enumerate(nestedLists):
            nodeId = 'node{}'.format(i)
            graph.node(nodeId, self._getLabelForList(llist))
            for j, elem in enumerate(llist):
                if isinstance(elem, list):
                    graph.edge(
                        '{}:{}:c'.format(nodeId, j),
                        'node{}'.format(nestedLists.index(elem)),
                    )
        if raw:
            return graph
        self._displayGraph(graph)

    def _findNestedLists(self, data, result=None):
        """
        Finds every nested array in the supplied data and returns is as a flat,
        one-dimensional list.

        :param data: The multi-dimensional list
        :type data: list
        :param result: The one-dimensional list holding the nested lists
        """
        if result is None:
            result = []
        if isinstance(data, list):
            result.append(data)
            for d in data:
                self._findNestedLists(d, result)
        return result
    
    def _getLabelForList(self, data):
        """
        Creates the label for a single graph node representing a list. This
        label is formatted as an HTML-like markup language specific to the
        Graphviz library.

        :param data: The list populating the label
        :type data: list
        """
        valuesTemp = '<TD PORT="{}">{}</TD>'
        indicesTemp = '<TD><FONT POINT-SIZE="8">{}</FONT></TD>'
        indices = [indicesTemp.format("["+self._toStr(i)+"]")
                   for i in range(len(data))]
        if len(indices) == 0:
            indices = [indicesTemp.format(" ")]
        indices = '\n'.join(indices)
        values = [valuesTemp.format(i, self._toStr(v))
                  for i, v in enumerate(data)]
        if len(values) == 0:
            values = [valuesTemp.format(0, " ")]
        values = '\n'.join(values)
        colspan = max(1, len(data))
        return LIST_TEMPLATE.format(
            colspan,
            len(data),
            indices,
            values
        )