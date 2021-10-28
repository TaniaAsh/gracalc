import tkinter as tk
from tkinter.constants import BOTTOM, E, EW, LEFT, N, RIGHT, S, SE, SW, W
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Graph Calculator")
        self.geometry("800x800")

        # Label with the status on the top of the window
        self.status_text = tk.StringVar()
        self.status_text.set("Status: Please input your expression and press RUN")
        self.label_text = tk.Label(self, textvariable=self.status_text)
        self.label_text.pack(padx=10, pady=10)

        # A frame for one entry and three buttons "help" "run" and "clear", all are inside the frame
        bottomframe = tk.Frame(self)
        bottomframe.pack( side = BOTTOM, padx=(20, 20), pady=(10, 10))

        help_button = tk.Button(bottomframe, text="Help", command=self.do_help)
        help_button.pack(side=LEFT, padx=(20, 20), pady=(10, 10))

        self.expression_var=tk.StringVar()
        self.expression_var.set("                                        ")
        name_entry = tk.Entry(bottomframe,textvariable = self.expression_var, font=('calibre',10,'normal'))
        name_entry.pack(side=LEFT, padx=(10, 10), pady=(10, 10))

        clear_button = tk.Button(bottomframe, text="Clear", command=self.do_clear)
        clear_button.pack(side=LEFT, padx=(10, 10), pady=(10, 10))

        run_button = tk.Button(bottomframe, text="Run", command=self.plot)
        run_button.pack(side=LEFT, padx=(10, 10), pady=(10, 10))
 
        # button that displays the plot
        #plot_button = Button(master = window, command = plot, height = 2, width = 10, text = "Plot")
  
    def do_run(self):
        self.status_text.set("Status: Runned")

    def do_clear(self):
        self.status_text.set("Status: Cleared")

    def do_help(self):
        self.status_text.set("Status: Helped")
        
    def plot(self):
        # First, we need to create the figure object using the Figure() class. 
        # Then, a Tkinter canvas(containing the figure) is created using FigureCanvasTkAgg() class. 
        # Matplotlib charts by default have a toolbar at the bottom. When working with Tkinter, however, 
        # this toolbar needs to be embedded in the canvas separately using the NavigationToolbar2Tk() class.
        
        # the figure that will contain the plot
        fig = Figure(figsize = (5, 5), dpi = 100)
    
        # list of squares
        y = [i**2 for i in range(101)]
    
        # adding the subplot
        plot1 = fig.add_subplot(111)
    
        # plotting the graph
        plot1.plot(y)
    
        # creating the Tkinter canvas
        # containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig, master = window)  
        canvas.draw()
    
        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().pack(padx=(10, 10), pady=(10, 10))
    
        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas, window)
        toolbar.update()
    
        # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().pack()

if __name__ == "__main__":
    window = Window()
    window.mainloop()
