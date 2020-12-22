from .templates import DICT_TEMPLATE
from graphviz import Digraph
import os


class Dict:

    def makeGraph(self, data):
        """
        Creates a graph to visualize of a Python dictionary

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
        return graph

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
            strKey = repr(key)
            strVal = repr(data[key])
            keyValuePairs.append(template.format(strKey, strVal))
        return DICT_TEMPLATE.format(
            len(data),
            "\n".join(keyValuePairs)
        )
