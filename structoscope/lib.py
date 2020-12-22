import io
import matplotlib.pyplot as plt
from PIL import Image

from .slist import List
from .sdict import Dict
from .stree import Tree


class Scope:
    """
    The Scope class is a wrapper around a single visualization window

    :param childMemberName: The name of the member containing the data of
                            the node object
    :type dataMemberName: str
    :param childrenMemberName: The name of the member containing the
                               children of the node object
    :type childrenMemberName: str
    """

    def __init__(self, dataMemberName=None, childrenMemberName=None):
        self.fig = None
        self.members = {
            'children': childrenMemberName,
            'data': dataMemberName
        }

    def print(self, data, raw=False):
        """
        Display a visualization of an arbitrary Python object.
        Supports lists, dictionaries and trees.

        :param data: The object to visualize
        :type data: Object
        :param raw: If true returns a string representing the
                    dot-notation graph
        :type raw: bool
        """

        graph = None
        if isinstance(data, list):
            s = List()
            graph = s.makeGraph(data)
        elif isinstance(data, dict):
            s = Dict()
            graph = s.makeGraph(data)
        else:
            s = Tree(self.members)
            graph = s.makeGraph(data)
        if raw:
            return graph
        self._displayGraph(graph)

    def _displayGraph(self, graph):
        """
        Converts the graph into a PNG image and displays it as a plot

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

    @staticmethod
    def wait(secs):
        """
        Block the main thread for any number of seconds

        :param secs: Amount of time to wait for, in seconds
        :type secs: float
        """
        plt.pause(secs)
