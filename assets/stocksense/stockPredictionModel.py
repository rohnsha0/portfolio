import requests
import streamlit as st

class stockPredictionModel():
    
    def __init__(self):
        self.timeframes= ["1D", "1H"]
        self.indices= ["NSE", "BSE"]
        self.dataset= ["ITC", "HDFC", "TCS", "INFY", "RELIANCE", "HDFCBANK", "ICICIBANK", "AXISBANK", "KOTAKBANK", "SBIN", "BAJFINANCE", "BAJAJFINSV", "HDFCLIFE"]
        self.responseCode= 999

    def predictStockPrice(self, symbol, isIntraday) -> str:
        progress = st.progress(0, text="Sending requests to server for stock predictions...")
        print(isIntraday)
        if isIntraday:
            print(symbol)
            data= requests.get(f"https://quuicqg435fkhjzpkawkhg4exi0vjslb.lambda-url.ap-south-1.on.aws/prediction/{symbol}")
            self.responseCode= data.status_code
            if self.responseCode == 200:
                progress.progress(100, text="Predictions are ready to be displayed")
                return format(data.json()["predicted_close"], ".2f")
            elif self.responseCode != 999 and self.responseCode != 200:
                progress.progress(100, text="Stock not found in the database")
                return "Stock not found"
        print(f"status code: {self.responseCode}")
        return "Feature unavailable"
