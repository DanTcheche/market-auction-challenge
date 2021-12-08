import os
import json
import pytest

from market_auction_challenge.market_auction_value_calculator import MarketAuctionCalculator

def __load_data():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../market_auction_challenge/utils/api-response.json')
    with open(filename) as api_response:
        data = json.load(api_response)
        return data


def test_correct_input():
    data = __load_data()
    result = MarketAuctionCalculator(data).calculate_for_model_and_year(67352, 2007)
    market_ratio_for_2007 = 0.317628
    auction_ratio_for_2007 = 0.185085
    cost_for_67352 = 681252
    assert result['marketValue'] == market_ratio_for_2007 * cost_for_67352
    assert result['auctionValue'] == auction_ratio_for_2007 * cost_for_67352


def test_incorrect_id():
    data = __load_data()
    with pytest.raises(ValueError) as error:
        MarketAuctionCalculator(data).calculate_for_model_and_year(87964, 2011)
        assert error.msg =="No data loaded for that model id"


def test_non_existant_year():
    with pytest.raises(ValueError) as error:
        data = __load_data()
        MarketAuctionCalculator(data).calculate_for_model_and_year(67352, 1910)
        assert error.msg == "No data loaded for that year"


def test_invalid_data():
    invalid_data = {'invalid_data': 789}
    with pytest.raises(ValueError) as error:
        MarketAuctionCalculator(invalid_data).calculate_for_model_and_year(67352, 1910)
        assert error.msg == "Invalid data loaded"
