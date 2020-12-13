import io
import os

import matplotlib.pyplot as plt
from graphviz import Digraph
from PIL import Image


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


class Scope:
    """
    The Scope class is a wrapper around a single visualization window
    """

    def __init__(self, dataMemberName=None, childrenMemberName=None):
        """
        :param childMemberName: The name of the member containing the data of
        the node object
        :type dataMemberName: str
        :param childrenMemberName: The name of the member containing the
        children of the node object
        :type childrenMemberName: str
        """
        self.fig = None
        self.members = {
            'children': childrenMemberName,
            'data': dataMemberName
        }

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

    def printDict(self, data, raw=False):
        """
        Creates a visualization of a Python dictionary

        :param data: The dictionary to visualize
        :type data: dict
        """

        if not isinstance(data, dict):
            raise ValueError('invalid argument type: {}'.format(type(data)))
        try:
            tempFolder = os.environ['TMPDIR']
        except Exception:
            tempFolder = "."
        graph = Digraph('dict_graph',
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
        graph.node('node0', self._getLabelForDict(data))
        if raw:
            return graph
        self._displayGraph(graph)

    def printTree(self, data, raw=False):
        """
        Creates a visualization of a tree

        :param data: The root object of the tree to visualize
        :type data: Object
        """

        try:
            tempFolder = os.environ['TMPDIR']
        except Exception:
            tempFolder = "."
        graph = Digraph('tree_graph',
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
        children = self._findChildren(data)
        for i, node in enumerate(children):
            nodeId = 'node{}'.format(i)
            graph.node(nodeId, self._getLabelForNode(node))
            for j, elem in enumerate(getattr(node, self.members['children'])):
                graph.edge(
                    '{}:{}:c'.format(nodeId, j),
                    'node{}'.format(children.index(elem)),
                )
        if raw:
            return graph
        self._displayGraph(graph)

    def _displayGraph(self, graph):
        """
        Converts the graph into a PNG image and displays it a plot

        :param graph: The graph object to display
        :type graph: graphviz.Digraph
        """
        pngBytes = graph.pipe(format='png')
        pngImage = Image.open(io.BytesIO(pngBytes))
        if self.fig is None:
            _, self.fig = plt.subplots(1)
            self.fig.axis('off')
        self.fig.imshow(pngImage, aspect='equal')
        plt.show(block=False)
        plt.pause(0.1)

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

    def _findChildren(self, data, result=None):
        """
        Finds every node in the supplied tree and returns is as a flat,
        one-dimensional list.

        :param data: The root of the tree
        :type data: Object
        :param result: The one-dimensional list holding the nodes
        """
        if result is None:
            result = []
        if data is None:
            return
        result.append(data)
        for child in getattr(data, self.members['children']):
            self._findChildren(child, result)
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

    def _getLabelForDict(self, data):
        """
        Creates the label for a single graph node representing a dictionary.
        This label is formatted as an HTML-like markup language specific to the
        Graphviz library.

        :param data: The dictionary populating the label
        :type data: dict
        """

        template = '<TR><TD>{}</TD><TD>{}</TD></TR>'
        keyValuePairs = []
        for key in data:
            strKey = self._toStr(key)
            strVal = self._toStr(data[key])
            keyValuePairs.append(template.format(strKey, strVal))
        return DICT_TEMPLATE.format(
            len(data),
            "\n".join(keyValuePairs)
        )

    def _getLabelForNode(self, data):
        """
        Creates the label for a single graph node representing the node of a
        tree. This label is formatted as an HTML-like markup language specific
        to the Graphviz library.

        :param data: The node populating the label
        :type data: Object
        """

        portTemp = '<TD PORT="{}"> </TD>'
        children = getattr(data, self.members['children'])
        value = getattr(data, self.members['data'])
        ports = [portTemp.format(i) for i in range(len(children))]
        if len(children) == 0:
            ports = ['<TD COLSPAN="1">∅</TD>']
        colspan = max(1, len(children))
        return NODE_TEMPLATE.format(
            colspan,
            len(children),
            colspan,
            self._toStr(value),
            ''.join(ports)
        )

    def _toStr(self, value):
        """
        Convert a primitive type a string representation that is suitable for
        visualization.

        :param value: The value to convert to string
        """
        if isinstance(value, str):
            return '"{}"'.format(value)
        if isinstance(value, list):
            return " "
        return str(value)

    @staticmethod
    def wait(secs):
        """
        Block the main thread for any number of seconds

        :param secs: Amount of time to wait for, in seconds
        :type secs: float
        """
        plt.pause(secs)
