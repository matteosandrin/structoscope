from graphviz import Digraph
import os
import io
from PIL import Image
import matplotlib.pyplot as plt

LIST_TEMPLATE = '''<
<TABLE ALIGN="CENTER"
       BORDER="0"
       CELLBORDER="1"
       CELLSPACING="0"
       CELLPADDING="4">
    <TR>
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
</TABLE>
>'''


class Scope:

    def __init__(self, title):
        self.fig = None
        self.title = title

    def printList(self, data):
        if not isinstance(data, list):
            raise ValueError('invalid argument type: {}'.format(type(data)))

        tempFolder = os.environ['TMPDIR']

        graph = Digraph('list_graph',
                        directory=tempFolder,
                        node_attr={'shape': 'none'},
                        graph_attr={'dpi': '300'})
        graph.format = 'svg'
        graph.node('node0', self._getLabelForList(data))
        graph.edges([])

        pngBytes = graph.pipe(format='png')
        pngImage = Image.open(io.BytesIO(pngBytes))

        if self.fig is None:
            _, self.fig = plt.subplots(1)
            self.fig.axis('off')
        self.fig.imshow(pngImage, aspect='equal')
        plt.show(block=False)
        plt.pause(0.1)

    def _getLabelForList(self, data):
        valuesTemp = '<TD>{}</TD>'
        indicesTemp = '<TD><FONT POINT-SIZE="8">{}</FONT></TD>'
        indices = [indicesTemp.format("["+self._toStr(i)+"]")
                   for i in range(len(data))]
        if len(indices) == 0:
            indices = [indicesTemp.format(" ")]
        indices = '\n'.join(indices)
        values = [valuesTemp.format(self._toStr(v))
                  for v in data]
        if len(values) == 0:
            values = [valuesTemp.format(" ")]
        values = '\n'.join(values)
        colspan = max(1, len(data))
        return LIST_TEMPLATE.format(
            colspan,
            self.title,
            len(data),
            indices,
            values
        )

    def _toStr(self, value):
        if isinstance(value, str):
            return '"{}"'.format(value)
        return str(value)

    @staticmethod
    def wait(secs):
        plt.pause(secs)
