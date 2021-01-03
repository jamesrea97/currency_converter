from view import View
from model import Model
from currencies import CURRENCIES


class CurrencyConverter():
    def __init__(self):
        self.model = Model()
        self.view = View(self, CURRENCIES)

        self.view.run()

    def convert(self, c_in, v_in, c_out):
        ''' Controls conversion between Model and View '''
        currency_value, log_value = self.model.convert(c_in, v_in, c_out)
        self.view.update_view(currency_value, log_value)
