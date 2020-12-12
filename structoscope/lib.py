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
<B>{}</B><BR/>
<FONT POINT-SIZE="8">length: {}</FONT>
</TD>
    </TR>
    <TR>
{}
    </TR>
    <TR>
{}
    </TR>
''')

DICT_TEMPLATE = GENERAL_TEMPLATE.format('''<TR>
<TD COLSPAN="2">
<B>{}</B><BR/>
<FONT POINT-SIZE="8">length: {}</FONT>
</TD>
</TR>
<TR>
    <TD><B>key</B></TD>
    <TD><B>value</B></TD>
</TR>
{}
''')


class Scope:
    """
    The Scope class is a wrapper around a single visualization window

    :param title: The name of the object to visualize
    :type title: string
    """

    def __init__(self, title):
        self.fig = None
        self.title = title

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
            if i == 0:
                graph.node(nodeId, self._getLabelForList(llist, self.title))
            else:
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
        graph.node('node0', self._getLabelForDict(data, self.title))
        if raw:
            return graph
        self._displayGraph(graph)

    def _displayGraph(self, graph):
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

    def _getLabelForList(self, data, title=None):
        """
        Creates the label for a single graph node representing a list. This
        label is formatted as an HTML-like markup language specific to the
        Graphviz library.

        :param data: The list poplating the label
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
            title if title is not None else "list",
            len(data),
            indices,
            values
        )

    def _getLabelForDict(self, data, title=None):
        template = '<TR><TD><B>{}</B></TD><TD>{}</TD></TR>'
        keyValuePairs = []
        for key in data:
            strKey = self._toStr(key)
            strVal = self._toStr(data[key])
            keyValuePairs.append(template.format(strKey, strVal)) 
        return DICT_TEMPLATE.format(
            title if title is not None else "dict",
            len(data),
            "\n".join(keyValuePairs)
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
