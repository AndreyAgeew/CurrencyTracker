from pycbrf import ExchangeRates
from datetime import datetime, timezone
from decimal import Decimal


def get_currency_data(currency: str = 'USD') -> Decimal:
    """
    Получает данные о курсе заданной валюты.

    :param currency: Код валюты (например, 'USD', 'EUR', 'GBP').
    :return: Курс заданной валюты относительно рубля.
    """
    current_date = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    rates = ExchangeRates(current_date)
    currency_data = list(filter(lambda el: el.code == currency, rates.rates))[0].rate
    return Decimal(currency_data)
