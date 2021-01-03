import datetime
from scrapper import CurrencyScrapper


class CurrencyConversionSnapshot:
    def __init__(self, cur_out, conversion, timestamp, cur_in='EUR'):
        self.cur_in = cur_in
        self.cur_out = cur_out
        self.conversion = conversion
        self.timestamp = timestamp


class Model:
    def __init__(self):
        self.fx = self._update_cache()

    def convert(self, currency_in, value_in, currency_out):
        result = None
        string = None
        time = None
        try:
            if datetime.datetime.now() - self.fx[0].timestamp > datetime.timedelta(days=1):
                self._update_cache()

            value_in = float(value_in)

            if value_in > 0:
                for f in self.fx:
                    if f.cur_out == currency_in:
                        result = value_in / float(f.conversion)
                        time = f.timestamp
                for f in self.fx:
                    if f.cur_out == currency_out:
                        result = result * float(f.conversion)
            else:
                raise ValueError
        except ValueError:
            string = 'Must be a positive decimal.'
        else:
            string = 'Taken from cache with date {}'.format(time)
        finally:
            return result, string

    def _update_cache(self):
        return CurrencyScrapper.scrape()
