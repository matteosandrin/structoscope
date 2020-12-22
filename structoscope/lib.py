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
