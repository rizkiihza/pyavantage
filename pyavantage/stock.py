from client import Client
import constants

class AVStock(object):
    def __init__(self, api_key):
        self.client = Client()
        self.api_key = api_key

    def transform(self, stock_json):
        stock_data = {
                        'Date': [],
                        'Open': [],
                        'Close': [],
                        'High': [],
                        'Low': [],
                    }

        for date in stock_json:
            stock_data['Date'].append(date)

            for category in stock_json[date]:

                if 'open' in category:
                    stock_data['Open'].append(stock_json[date][category])
                if 'close' in category:
                    stock_data['Close'].append(stock_json[date][category])
                if 'high' in category:
                    stock_data['High'].append(stock_json[date][category])
                if 'low' in category:
                    stock_data['Low'].append(stock_json[date][category])

        return stock_data

    def process_data(self, response):
        price_key = ""
        for key in response:
            k_str = str(key)
            if constants.TIME_SERIES_KEY in k_str:
                price_key = k_str

        if price_key == "":
            raise Exception("No Price Data")

        return self.transform(response[price_key])

    def get_path_from_params(self, params):
        path = ""
        for key in params:
            path += "&" + str(key) + "=" +str(params[key])
        path += "&" + "apikey" + "=" + str(self.api_key)
        return path

    def get_function(self, period):
        function = "function="
        available_period = [constants.FUNCTION_DAILY, constants.FUNCTION_INTRADAY,
                            constants.FUNCTION_MONTHLY, constants.FUNCTION_WEEKLY]
        if period in available_period:
            return function + constants.FUNCTION_TIME_SERIES + '_' + period
        else:
            raise Exception("Period not available")

    def get_stock_data(self,  period, symbol,  params={}):
        params['symbol'] = symbol
        path = self.get_function(period) + self.get_path_from_params(params)

        json_response = self.client.get_response(path)
        stock_data = self.process_data(json_response)
        return stock_data