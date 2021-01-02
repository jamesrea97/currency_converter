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
        self._create_window()

    def _create_window(self):
        ''' Creates Window for App '''
        self.root = tk.Tk()
        self._create_intro_text()
        self._create_currency_selector()
        self._create_convert_button()
        tk.mainloop()

    def _create_intro_text(self):
        ''' Creates Introduction Text at top of Window '''
        intro_text = tk.Text(self.root, height=2, width=35)
        intro_text.insert(
            tk.END, "Welcome! This Program allows you to convert Currencies in real time!")
        intro_text.pack()

    def _create_currency_selector(self):
        ''' Creates Currency Selector for User '''

        self.currency_in_selector = tk.StringVar(self.root)
        self.currency_in_selector.set('GBP')
        self.currency_out_selector = tk.StringVar(self.root)
        self.currency_out_selector.set('GBP')

        self.currency_in = tk.OptionMenu(
            self.root, self.currency_in_selector, *self.choices)
        self.currency_out = tk.OptionMenu(
            self.root, self.currency_out_selector, *self.choices)

        label_in = tk.Label(text='Convert from:')
        label_out = tk.Label(text='Convert to:')

        self.value_in = tk.Entry(self.root, bd=4)

        label_in.pack()
        self.currency_in.pack()
        self.value_in.pack()
        label_out.pack()
        self.currency_out.pack()

    def _create_convert_button(self):
        ''' Creates Conversion button for User - callback in controller.py'''
        self.value_out = tk.Entry(self.root, bd=4)

        self.convert = tk.Button(
            self.root,
            text='Convert',
            command=partial(self._convert)
        )
        self.convert.pack()
        self.value_out.pack()

    def _convert(self):
        self.controller.convert(
            self.currency_in_selector.get(),
            self.value_in.get(),
            self.currency_out_selector.get(),
            self.value_out
        )
