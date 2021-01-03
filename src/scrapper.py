import requests
from bs4 import BeautifulSoup
import datetime
import model

CURRENCIES_WEBSITE = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml'


class CurrencyScrapper:

    @classmethod
    def scrape(cls):
        ''' Method scrapes currencies '''
        conversions = []
        try:
            soup = cls._get_soup(CURRENCIES_WEBSITE)
            fx_scrape = soup.find('cube')

            fx_time_snapshot = fx_scrape.contents[1].attrs['time']

            for entry in fx_scrape.contents[1].contents:
                if entry != '\n':
                    conversions.append(
                        model.CurrencyConversionSnapshot(
                            cur_out=entry.attrs['currency'],
                            conversion=entry.attrs['rate'],
                            timestamp=datetime.datetime.strptime(
                                fx_time_snapshot, '%Y-%m-%d')
                        )
                    )

        except requests.exceptions.ConnectionError:
            return 'Internet lost - could not fetch from {}'.format(websites.NEWS_HEADLINE)
        else:
            return conversions

    @ classmethod
    def _get_soup(csl, url):
        ''' Private-like method returning soup for given url '''
        page = requests.get(url)
        return BeautifulSoup(page.content, 'html.parser')
