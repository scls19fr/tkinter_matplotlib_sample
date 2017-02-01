import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random


class App(tk.Tk):
    def __init__(self, parent=None):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.title("A Matplotlib graph inside a Tkinter Python GUI app")

        button = tk.Button(self, text="Quit", command=self.on_click)
        button.grid(row=1, column=0)

        self.mu = tk.DoubleVar()
        self.mu.set(5.0)  # default value for parameter "mu"
        slider_mu = tk.Scale(self,
                             from_=7, to=0, resolution=0.1,
                             label='mu', variable=self.mu,
                             command=self.on_change
                             )
        slider_mu.grid(row=0, column=0)

        self.n = tk.IntVar()
        self.n.set(512)  # default value for parameter "n"
        slider_n = tk.Scale(self,
                            from_=512, to=2,
                            label='n', variable=self.n, command=self.on_change
                            )
        slider_n.grid(row=0, column=1)

        fig = Figure(figsize=(6, 4), dpi=96)
        ax = fig.add_subplot(111)
        x, y = self.data(self.n.get(), self.mu.get())
        self.line1, = ax.plot(x, y)

        self.graph = FigureCanvasTkAgg(fig, master=self)
        canvas = self.graph.get_tk_widget()
        canvas.grid(row=0, column=2)

    def on_click(self):
        self.quit()

    def on_change(self, value):
        x, y = self.data(self.n.get(), self.mu.get())
        self.line1.set_data(x, y)  # update data

        # set plot limit
        # ax = self.graph.figure.axes[0]
        # ax.set_xlim(min(x), max(x))
        # ax.set_ylim(min(y), max(y))

        # update graph
        self.graph.draw()

    def data(self, n, mu):
        lst_y = []
        for i in range(n):
            lst_y.append(mu * random.random())
        return range(n), lst_y


if __name__ == "__main__":
    app = App()
    app.mainloop()
