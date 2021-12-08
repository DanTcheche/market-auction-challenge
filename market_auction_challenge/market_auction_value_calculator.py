class MarketAuctionCalculator:

    def __init__(self, data):
        self.data = data

    def calculate_for_model_and_year(self, model_id, year):
        data_for_model = self.data.get(f'{model_id}', None)
        if not data_for_model:
            raise ValueError("No data loaded for that model id")
        try:
            cost_for_model = data_for_model['saleDetails']['cost']
            data_for_model_and_year = data_for_model['schedule']['years'].get(f'{year}', None)

            if not data_for_model_and_year:
                raise ValueError("No data loaded for that year")
            return {
                'marketValue': cost_for_model * data_for_model_and_year['marketRatio'],
                'auctionValue': cost_for_model * data_for_model_and_year['auctionRatio']
            }
        except KeyError:
            raise ValueError("Invalid data loaded")
