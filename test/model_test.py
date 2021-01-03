import datetime
import unittest
from unittest.mock import patch
import context
import model


class ShouldConvertCurrencies(unittest.TestCase):

    @classmethod
    def setUp(cls):
        ''' Sets up Model and Mock functions '''
        with patch.object(model.Model, '_update_cache') as mock_method:
            mock_method.return_value = [
                model.CurrencyConversionSnapshot(
                    'GBP', 1.5, datetime.datetime.now()),
                model.CurrencyConversionSnapshot(
                    'USD', 2.5, datetime.datetime.now())
            ]
            cls.model = model.Model()
            print(cls.model.fx)

    def test_converts_currencies(self):
        self.assertEqual(self.model.convert(
            'GBP', 9, 'USD')[0], 15.0)
        self.assertEqual(self.model.convert(
            'GBP', 'q', 'USD')[0], None)


if __name__ == "__main__":
    unittest.main()
