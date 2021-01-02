import controller
import datetime


class CurrencyConversionSnapshot:
    def __init__(self, cur_in, cur_out, conversion, timestamp):
        self.cur_in = cur_in
        self.cur_out = cur_out
        self.conversion = conversion
        self.timestamp = timestamp


class Model:
    def __init__(self):
        self.currencies = controller.CURRENCIES
        self.fx = self._create_fx()

    def convert(self, currency_in, value_in, currency_out):
        try:
            value_in = float(value_in)

            for snapshot in self.fx:
                if snapshot.cur_in == currency_in and snapshot.cur_out == currency_out:
                    if (datetime.datetime.now() - snapshot.timestamp) < datetime.timedelta(20):
                        return value_in * snapshot.conversion
        except ValueError:
            return 'Must be a decimal.'

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
