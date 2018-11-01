import unittest
import sys, os
from stock import AVStock
from technical_analysis import AVTechnicalAnalysis

class TestStock(unittest.TestCase):
    def test_params(self):
        av = AVStock("demo")
        params = {
            "symbol": "MSFT",
            "period": "WEEKLY"
        }
        path = av.get_path_from_params(params)
        self.assertTrue("symbol" in path)
        self.assertTrue("period" in path)
        self.assertTrue("apikey" in path)

    def test_get_stock_daily(self):
        av = AVStock("SW8DH9H0EQ77YZEV")
        result = av.get_stock_data("MSFT", "DAILY")
        keys = list(result.keys())
        self.assertEqual(len(keys), 5)

    def test_get_stock_intraday(self):
        av = AVStock("SW8DH9H0EQ77YZEV")
        result = av.get_stock_data("MSFT", "INTRADAY", {"interval": "5min"})
        keys = list(result.keys())
        self.assertEqual(len(keys), 5)

    def test_get_stock_weekly(self):
        av = AVStock("SW8DH9H0EQ77YZEV")
        result = av.get_stock_data("MSFT", "WEEKLY")
        keys = list(result.keys())
        self.assertEqual(len(keys), 5)

    def test_get_stock_monthly(self):
        av = AVStock("SW8DH9H0EQ77YZEV")
        result = av.get_stock_data("MSFT", "MONTHLY")
        keys = list(result.keys())
        self.assertEqual(len(keys), 5)

class TestTechnicalAnalysis(unittest.TestCase):
    def test_params(self):
        av = AVTechnicalAnalysis("SW8DH9H0EQ77YZEV")
        params = {
            "function": "MACD",
            "symbol": "MSFT",
            "interval": "weekly",
            "series_type": "open"
        }
        path = av.get_path_from_params(params)
        self.assertTrue("function" in path)
        self.assertTrue("symbol" in path)
        self.assertTrue("interval" in path)
        self.assertTrue("series_type" in path)
        self.assertTrue("apikey" in path)

    def test_macd(self):
        av = AVTechnicalAnalysis("SW8DH9H0EQ77YZEV")
        result = av.get_stock_data("MACD", "MSFT")
        list_keys = list(result.keys())
        self.assertEqual(len(list_keys), 4)
        self.assertTrue('Date' in list_keys)
        self.assertTrue('MACD' in list_keys)

    def test_rsi(self):
        av = AVTechnicalAnalysis("SW8DH9H0EQ77YZEV")
        result = av.get_stock_data("RSI", "MSFT")
        list_keys = list(result.keys())
        self.assertEqual(len(list_keys), 2)
        self.assertTrue('Date' in list_keys)
        self.assertTrue('RSI' in list_keys)

    def test_stoch(self):
        av = AVTechnicalAnalysis("SW8DH9H0EQ77YZEV")
        result = av.get_stock_data("STOCH", "MSFT")
        list_keys = list(result.keys())
        self.assertEqual(len(list_keys), 3)
        self.assertTrue('SlowK' in list_keys)
        self.assertTrue('SlowD' in list_keys)

if __name__ == '__main__':
    unittest.main()