import requests

class stockPredictionModel():
    
    def __init__(self):
        self.timeframes= ["1D", "1H"]
        self.dataset= ["ITC", "HDFC", "TCS", "INFY", "RELIANCE", "HDFCBANK", "ICICIBANK", "AXISBANK", "KOTAKBANK", "SBIN", "BAJFINANCE", "BAJAJFINSV", "HDFCLIFE"]
        self.responseCode= 999

    def predictStockPrice(self, symbol, isIntraday) -> str:
        print(isIntraday)
        if isIntraday:
            data= requests.get(f"https://quuicqg435fkhjzpkawkhg4exi0vjslb.lambda-url.ap-south-1.on.aws/prediction/{symbol}.NS")
            self.responseCode= data.status_code
            if self.responseCode == 200:
                print(format(data.json()["predicted_close"], ".2f"))
