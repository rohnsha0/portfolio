import streamlit as st
import os

st.set_page_config(
    page_title="Rohan Shaw: StockSense",
    page_icon=os.path.join("assets", "stocksense-favicon.png"),
    layout="centered",
    initial_sidebar_state="collapsed"
)

# hide the hamburger menu
hide_decoration_bar_style = '''<style>header {visibility: hidden;}</style>'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

with open(
        os.path.join("assets", "styles.css")
) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

st.image(os.path.join("assets", "stocksense_banner.png"))
st.title('About StockSense')
st.write("""
    Welcome to StockSense, an open-source app leveraging advanced deep neural networks for precise stock price predictions. Empower your investment decisions with cutting-edge technology and collaborative development.
""")
st.link_button("View on Github", url="https://github.com/rohnsha0/stocksense", type="primary")

st.header("AI-based Stock Price Prediction")
st.write("""The flagship feature of the project where users can search for their preferred stocks to get a detailed 
idea for the future stock price using sophisticated LSTM neural network. It is based upon temporal data that updated 
frequently. """)
with st.expander("Get a hands-on experience on the stock price prediction"):
    st.write('''When you input the symbol, we will search for the symbol into the database of supported stocks and 
    then if match found, we will proceed with predicting prices either for 1H or 1D time frames''')
    col1, col2 = st.columns([3, 2])
    with col1:
        index_selector= ['NSE', 'BSE']
        st.selectbox("Select an index to predict stocks from", index_selector)
    with col2:
        index_selector = ['1D', '1H']
        st.selectbox("Select a time horizon", index_selector, index=None)
    st.text_input("Enter a symbol to continue")
    isPredicting= st.button("Predict Prices")
    if isPredicting: st.error("Feature unavailable")
st.subheader("How it works?")
