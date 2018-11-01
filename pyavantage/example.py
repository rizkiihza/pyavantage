from stock import AVStock
from technical_analysis import AVTechnicalAnalysis

def print_head(result):
    keys = list(result.keys())
    for i in range(10):
        for key in keys:
            print(result[key][i], end=" ")
        print()

if __name__ == '__main__':
    avStock = AVStock("SW8DH9H0EQ77YZEV")
    aVTechnicalAnalysis = AVTechnicalAnalysis("SW8DH9H0EQ77YZEV")

    # daily stock price
    microsoft_stock = avStock.get_stock_data("DAILY", "MSFT")
    print_head(microsoft_stock)

    # stochastic technical indicator
    microsoft_stochastic = aVTechnicalAnalysis.get_stock_data("STOCH", "MSFT")
    print_head(microsoft_stochastic)

    # rsi technical indicator
    microsoft_rsi = aVTechnicalAnalysis.get_stock_data("RSI", "MSFT")
    print_head(microsoft_rsi)