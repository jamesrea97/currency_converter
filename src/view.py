import tkinter as tk
from functools import partial


class View:

    def __init__(self, controller, choices):
        ''' Instantiates the controller needed for callback '''
        self.choices = choices
        self.controller = controller
        self.root = None
        self.currency_in = None
        self.currency_out = None
        self.value_in = None
        self.value_out = None
        self.convert = None
        self.log_text = None
        self.create_window()

    def create_window(self):
        ''' Creates Window for App '''
        self.root = tk.Tk()
        self.create_intro_text()
        self.create_currency_selector()
        self.create_log_text()
        self.create_convert_button()
        tk.mainloop()

    def create_intro_text(self):
        ''' Creates Introduction Text at top of Window '''
        intro_text = tk.Text(self.root, height=2, width=35)
        intro_text.insert(
            tk.END, "Welcome! This Program allows you to convert Currencies in real time!")
        intro_text.pack()

    def create_currency_selector(self):
        ''' Creates Currency Selector for User '''
        variable = tk.StringVar(self.root)
        variable.set('GBP')

        self.currency_in = tk.OptionMenu(self.root, variable, *self.choices)
        self.currency_out = tk.OptionMenu(self.root, variable, *self.choices)

        label_in = tk.Label(text='Convert from:')
        label_out = tk.Label(text='Convert to:')

        self.value_in = tk.Entry(self.root, bd=4)

        label_in.pack()
        self.currency_in.pack()
        self.value_in.pack()
        label_out.pack()
        self.currency_out.pack()

    def create_convert_button(self):
        ''' Creates Conversion button for User - callback in controller.py'''
        self.value_out = tk.Entry(self.root, bd=4)

        self.convert = tk.Button(
            self.root,
            text='Convert',
            command=partial(self.controller.callback,
                            self.currency_in,
                            self.value_in,
                            self.currency_out,
                            self.value_out,
                            self.log_text
                            )
        )
        self.convert.pack()
        self.value_out.pack()

    def create_log_text(self):
        ''' Creates a log text for User '''
        self.log_text = tk.Text(self.root, height=2, width=30)
        self.log_text.insert(
            tk.END, "Please select fields.")
        self.log_text.pack(side=tk.BOTTOM)
