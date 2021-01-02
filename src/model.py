

class CurrencyConversionSnapshot:
    def __init__(self, cur_in, cur_out, conversion, timestamp):
        self.cur_in = min(cur_in, cur_out)
        self.cur_out = max(cur_in, cur_out)


class Model:
    def convert(self, currency_in, value_in, currency_out, log_text):
        return 2
