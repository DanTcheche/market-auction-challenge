import json
import os

from market_auction_challenge.market_auction_value_calculator import MarketAuctionCalculator


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'utils/api-response.json')
    with open(filename) as api_response:
        data = json.load(api_response)
        result = MarketAuctionCalculator(data).calculate_for_model_and_year(87390, 2016)
        print(result)


if __name__ == '__main__':
    main()
