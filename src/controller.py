from view import View
from model import Model

CURRENCIES = ['GBP', 'EUR', 'USD']


class CurrencyConverter():
    def __init__(self):
        self.model = Model()
        self.view = View(self, CURRENCIES)

    def convert(self, c_in, v_in, c_out, widget_out, log_text):

        value = self.model.convert(c_in, v_in, c_out, log_text)
        widget_out.delete(0, "end")
        widget_out.insert(0, value)
