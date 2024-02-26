import streamlit as st
import os
from assets.stocksense.stockPredictionModel import stockPredictionModel
import yfinance as yf

st.set_page_config(
    page_title="Rohan Shaw: StockSense",
    page_icon=os.path.join("assets", "stocksense", "stocksense-favicon.png"),
    layout="centered",
    initial_sidebar_state="collapsed"
)

with st.sidebar:
    st.subheader("Contents in the page")
    st.write("""
            - [About StockSense](#about-stocksense)
            - [Features](#features)
                - [AI-based Stock Price Prediction](#ai-based-stock-price-prediction) 
            - [How it works?](#how-it-works)
                - [Data Collection](#data-collection)
                - [Data Preprocessing & Model Building](#data-preprocessing-model-building)
                - [Model Evaluation](#model-evaluation)
            - [Contributions](#contributions)
             """)

st.toast("Download **[mobile application](https://play.google.com/store/apps/details?id=com.rohnsha.stocksense)** for complete features.")

# hide the hamburger menu
hide_decoration_bar_style = '''<style>header {visibility: hidden;}</style>'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

with open(
        os.path.join("assets", "styles.css")
) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

st.image(os.path.join("assets", "stocksense", "stocksense_banner.png"))
st.title('About StockSense')
with st.container(border=True):
    s1, s2= st.columns(2)
    with s1:
        st.write("**Version:** 3.6 Rose Blooms (web)")
    with s2:
        st.write("**Build Number:** V2024.25.02.11")
st.write("""
    Welcome to StockSense, an open-source app leveraging advanced deep neural networks for precise stock price predictions. Empower your investment decisions with cutting-edge technology and collaborative development.
""")
st.link_button("View on Github", url="https://github.com/rohnsha0/stocksense", type="primary")

st.header("Features")
st.write("""
    Stocksense has various features to help you make informed decisions about your investments. Among which only the price prediction feature is available on the web. The other features are available on the mobile application.
""")
st.subheader("AI-based Stock Price Prediction")
st.write("""The flagship feature of the project where users can search for their preferred stocks to get a detailed 
idea for the future stock price using sophisticated LSTM neural network. It is based upon temporal data that updated 
frequently. """)
with st.expander("Get a hands-on experience on the stock price prediction"):
    st.write('''When you input the symbol, we will search for the symbol into the database of supported stocks and 
    then if match found, we will proceed with predicting prices either for 1H or 1D time frames''')
    col1, col2 = st.columns([3, 2])
    stockPredModel= stockPredictionModel()
    with col1:
        index_selector= st.selectbox("Select an index to predict stocks from", stockPredModel.indices, index=0)
    with col2:
        timeframe = st.selectbox("Select a time horizon", stockPredModel.timeframes, index=0)
    symbol_inp = st.selectbox("Enter a symbol to continue", stockPredModel.dataset, placeholder="Select a symbol", index=None)
    
    print(f"index-selector; {index_selector}")
    if symbol_inp != None:
        if index_selector==stockPredModel.indices[0]:
            symbol_inp= f"{symbol_inp}.NS"
        elif index_selector=="BSE":
            symbol_inp= f"{symbol_inp}.BO"

    print(f"selected symbol: {symbol_inp}")

    isPredicting = st.button("Predict Prices")

    print(symbol_inp)

    if isPredicting is True:

        if symbol_inp != None:
            data= stockPredModel.predictStockPrice(symbol=symbol_inp, isIntraday= True if timeframe == "1D" else False)

            if stockPredModel.responseCode == 200:
                cData = yf.download(symbol_inp, period="365d", interval="1d")
                #fChart= ff.create_candlestick(cData['Open'], cData['High'], cData['Low'], cData['Close'], dates=cData.index)
                #st.plotly_chart(fChart, use_container_width=True)
                st.line_chart(cData.drop(columns=['Volume']))                
                st.subheader("Stock Price Prediction")
                st.write(f"Predicted price for {symbol_inp.split('.')[0]} is {data}")

            if stockPredModel.responseCode != 200 and stockPredModel.responseCode != 999:
                st.warning("Either stock not found or the server is down. Please try again later.")
        else:
            st.error("Please select a symbol to continue")
    

st.header("How it works?")
st.write("""
        The stock price prediction is based on the Long Short-Term Memory (LSTM) neural network. Whenever any symbol is entered, we fetch relevant data i.e. price, trend, etc on either daily or hourly timeframe as selected for prediction, which is then fed into the custom trained LSTM model per stock on the backend. The model then predicts the future stock price based on the historical data and the current trend. The prediction is then displayed to the user.\n
         If daily time frame is selected, the model is trained on maximum available price data per stock which then predicts the stock price for the next day. If hourly time frame is selected, the model predicts the stock price for the next hour.
        """)
st.subheader("Data Collection")
st.write("""
    Since he data is fetched from Yahoo Finance official API, the symbols need to be appended with the index they belong to. For example, if you want to predict the stock price of Reliance Industries, you need to enter the symbol as RELIANCE.NS for NSE and RELIANCE.BO for BSE. 
    \nAfter getting the symbols ready and appended, we input the symbols into the yFinance python module with desired time interval i.e. 1D or 1H which then returns the data in the form of a pandas dataframe. 
""")
st.subheader("Data Preprocessing & Model Building")
codeBody= """
    Model: "sequential_1"
    _________________________________________________________________
    Layer (type)                Output Shape              Param #   
    =================================================================
    lstm_3 (LSTM)               (None, 14, 84)            28896     
                                                                    
    dropout_3 (Dropout)         (None, 14, 84)            0         
                                                                    
    lstm_4 (LSTM)               (None, 14, 64)            38144     
                                                                    
    dropout_4 (Dropout)         (None, 14, 64)            0         
                                                                    
    lstm_5 (LSTM)               (None, 50)                23000     
                                                                    
    dropout_5 (Dropout)         (None, 50)                0         
                                                                    
    dense_1 (Dense)             (None, 1)                 51        
                                                                    
    =================================================================
    Total params: 90,091
    Trainable params: 90,091
    Non-trainable params: 0
    _________________________________________________________________
"""
st.write("""
    The data is then preprocessed and cleaned to remove any null values and then the data is split into training and testing data. After which the data is scaled using MinMaxScaler from scikit-learn. The scaled data is then reshaped into a 3D array to be fed into the LSTM model. 
    \nThe model is then trained on the training data and then tested on the testing data. The general model structure for the project is as follows:
""")
st.code(codeBody, language="python")
st.write("""
    The model is trained on 150 epoch with average batch of 32. In addition to which, the Adam optimizer is used with mean squared error as the loss function. 
""")
st.subheader("Model Evaluation")
st.write("""
    The model is evaluated on the testing data i.e. last 90 days, and the results are then compared with the actual data to check the accuracy of the model. The model is then saved and used for the prediction of the stock price. If the model is not performing well, it is retrained on the new data and then saved for future use.
""")
st.header("Contributions")
st.write("""
    The project is open-source and is available on GitHub. You can contribute to the project by forking the repository and then creating a pull request. The project is open to all kinds of contributions i.e. bug fixes, feature addition, documentation, etc.
    \nPost to the issues for any bugs, feature requests or any discussions about either [web](https://github.com/rohnsha0/stocksense) or [android app](https://play.google.com/store/apps/details?id=com.rohnsha.stocksense) version of the project.
""")