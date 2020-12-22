from .templates import NODE_TEMPLATE
from graphviz import Digraph
import os


class Tree:

    def __init__(self, members):
        self.members = members

    def makeGraph(self, data):
        """
        Creates a graph to visualize a tree

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
        return graph

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
        if hasattr(data, self.members['children']):
            for child in getattr(data, self.members['children']):
                self._findChildren(child, result)
        return result

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
            repr(value),
            ''.join(ports)
        )
