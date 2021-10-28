import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Graph Calculator")

        self.status_text = tk.StringVar()
        self.status_text.set("Status: Please input your expression")
        self.label_text = tk.Label(self, textvariable=self.status_text)
        self.label_text.pack(fill=tk.BOTH, expand=1, padx=100, pady=50)
        
        self.expression_var=tk.StringVar()
        self.expression_var.set("   ")
        name_entry = tk.Entry(self,textvariable = self.expression_var, font=('calibre',10,'normal'))
        name_entry.pack()

        run_button = tk.Button(self, text="Run", command=self.do_run)
        run_button.pack(side=tk.RIGHT, padx=(20, 20), pady=(20, 20))

        clear_button = tk.Button(self, text="Clear", command=self.do_clear)
        clear_button.pack(side=tk.RIGHT, padx=(20, 20), pady=(20, 20))
    
        help_button = tk.Button(self, text="Help", command=self.do_help)
        help_button.pack(side=tk.LEFT, padx=(20, 20), pady=(20, 20))

    def do_run(self):
        self.status_text.set("Status: Runned")

    def do_clear(self):
        self.status_text.set("Status: Cleared")

    def do_help(self):
        self.status_text.set("Status: Helped")
        


if __name__ == "__main__":
    window = Window()
    window.mainloop()
