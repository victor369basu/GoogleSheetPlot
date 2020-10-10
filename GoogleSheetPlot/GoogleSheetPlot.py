from GoogleSheetPlot.application import access_sheet
from GoogleSheetPlot.graph import plot_graph
import pandas as pd
class GoogleSheetPlot:
    def __init__(self):
        """
        Initialize GoogleSheetPlot package
        """
        self.df = None
        self.plot = None
    def getDataFrame(self, SSI, SRN):
        """
        Args:
          SI: google Spreadsheet-ID, generated from the link of the google
              spreadsheet saved in google drive.
          RN: Range Name of the google spreadsheet you want to use. Ex-A1:c100
        Returns:
           Accessed google sheet in dataframe format.
        """
        sheet = access_sheet(SSI, SRN)
        self.df = pd.DataFrame(sheet()[1:], columns=sheet()[0])
        return self.df

    def getPlot(self, x=None, y=None, plot='scatter'):
        """
        plot the necessary graph from the dataframed google sheet.
        Args:
            x: The dataframe column to be plotted over the x-axis.
            y: The dataframe column to be plotted over the y-axis.
            plot: The category of a plot for visualization.
        Reurn:
           plot the necessary graph and save the graph the present directory.
        """
        if x==None or x=='':
            raise Exception(" Column-1 is missing.")
        if y==None or y=='':
            raise Exception(" Column-2 is missing.")
        graph = plot_graph(self.df, x, y)
        graph()
        graph.save()
