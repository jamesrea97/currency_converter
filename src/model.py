import controller
import datetime


class CurrencyConversionSnapshot:
    def __init__(self, cur_in, cur_out, conversion, timestamp):
        self.cur_in = cur_in
        self.cur_out = cur_out
        self.conversion = conversion
        self.timestampe = timestamp


class Model:
    def __init__(self):
        self.currencies = controller.CURRENCIES
        self.fx = self._create_fx()

    def convert(self, currency_in, value_in, currency_out, log_text):
        try:
            value_in = int(value_in)
        except:
            log_text.delete(0, "end")
            log_text.insert(0, 'Invalid Value. Must be a number')

    def _create_fx(self):
        fxs = []
        for c_in in self.currencies:
            for c_out in self.currencies:
                fx = None
                if c_in == c_out:
                    fx = 1
                fxs.append(CurrencyConversionSnapshot(
                    c_in, c_out, fx, datetime.datetime.now()))
        return fxs
