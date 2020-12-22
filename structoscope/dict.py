from lib import GENERAL_TEMPLATE
from graphviz import Digraph
import os

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


class Dict:

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
