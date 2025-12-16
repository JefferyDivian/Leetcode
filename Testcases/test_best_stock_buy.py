
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Solution.best_time_to_buy_and_sell_stocks import maxProfit
import pytest

@pytest.mark.parametrize(
    "prices, expected",
    [
        ([7, 1, 5, 3, 6, 4], 5),      # buy at 1, sell at 6
        ([7, 6, 4, 3, 1], 0),         # no profitable transaction
        ([1, 2, 3, 4, 5], 4),         # buy at 1, sell at 5
        ([3, 3, 5, 0, 0, 3, 1, 4], 4),# buy at 0, sell at 4
        ([1], 0),                    # single price
        ([], 0),                     # empty input
    ],
    ids=[
        "Standard profit case",
        "Monotonically decreasing",
        "Monotonically increasing",
        "Multiple valleys and peaks",
        "Single element",
        "Empty list",
    ]
)
def test_max_profit(prices, expected):
    assert maxProfit(prices) == expected