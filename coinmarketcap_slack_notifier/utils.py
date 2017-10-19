import json
from collections import namedtuple

from decimal import Decimal

ObservableCoin = namedtuple('ObservableCoin', 'id icon_url percent')
StoredCoin = namedtuple('StoredCoin', 'id price_usd price_btc total_supply percent')
ChangedCoin = namedtuple('ChangedCoin', 'id price_usd price_btc total_supply')
AttachmentData = namedtuple('AttachmentData', 'observable_coin coin_price_action coin_total_supply_action '
                                              'new_price_usd new_price_btc price_percent_change coin_amount_change '
                                              'btc_percent_change')


class ValueWasNotChanged(ValueError):
    pass


class CoinDoesNotExist(Exception):
    pass


def json_dumps(data):
    def default(obj):
        if isinstance(obj, Decimal):
            return float(obj)
    return json.dumps(data, default=default)
