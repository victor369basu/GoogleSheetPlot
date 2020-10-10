import matplotlib.pyplot as plt

class plot_graph:
    def __init__(self, dataFrame=None, x=None, y=None, plot='scatter'):
        """
        plot the necessary graph from the dataframed google sheet.
        Args:
            dataFrame: dataframe to be used for visualization.
            x: The dataframe column to be plotted over the x-axis.
            y: The dataframe column to be plotted over the y-axis.
            plot: The category of a plot for visualization.
        Returns:
            Initialized parameter for plotting the necessary graph.
        """
        self.x = x
        self.y = y
        self.col1 = dataFrame[x]
        self.col2 = dataFrame[y]
        self.plot = plot
        self.plt = None
        self.container={
        'scatter',
        'line',
        'bar'
        }

    def __call__(self):
        """
        plot the necessary graph.
        """
        if self.plot not in self.container:
            raise Exception("Plot category does not exist. Please select among the following: {}".format(self.container))
        plt.figure(figsize=(18,18))
        if self.plot == 'scatter':
            plt.scatter(self.col1,self.col2)
        if self.plot == 'line':
            plt.plot(self.col1,self.col2)
        if self.plot == 'bar':
            plt.bar(self.col1,self.col2)
        plt.xlabel(self.x,fontsize=18)
        plt.ylabel(self.x,fontsize=18)
        plt.title("{}_{}_{}".format(self.x,self.y,self.plot),fontsize=18)
        self.plt = plt
        plt.show()

    def save(self):
        """
        Save the visualized graph in a .png file.
        """
        if self.plt==None:
            raise Exception("Matplotlib.pyplot not initialized.")
        plt.savefig("{}_{}_{}.png".format(self.x,self.y,self.plot))
        print("Saved Image Successfully.")
