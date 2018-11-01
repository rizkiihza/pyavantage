from client import Client
import constants

class AVTechnicalAnalysis(object):
    def __init__(self, api_key):
        self.client = Client()
        self.api_key = api_key

    def get_keys(self, stock_json):
        keys = list(stock_json.keys())
        if len(keys) == 0:
            raise Exception("No price data")
        return stock_json[keys[0]].keys()

    def transform(self, stock_json):
        price_keys = list(self.get_keys(stock_json))

        stock_data = {'Date' : []}

        for key in price_keys:
            stock_data[key] = []

        for date in stock_json:
            stock_data['Date'].append(date)

            for category in stock_json[date]:
                stock_data[category].append(stock_json[date][category])

        return stock_data

    def process_data(self, response):
        price_key = ""
        for key in response:
            k_str = str(key)
            if constants.TA_KEY in k_str:
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


    def get_stock_data(self, function, symbol, interval='daily', time_period='5',
                        series_type='close', params={}):

        params['function'] = function
        params['symbol'] = symbol
        params['interval'] = interval
        params['time_period'] = time_period
        params['series_type'] = series_type

        path = self.get_path_from_params(params)

        json_response = self.client.get_response(path[1:])
        stock_data = self.process_data(json_response)

        return stock_data

