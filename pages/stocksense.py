import streamlit as st
import os

st.set_page_config(
    page_title="Rohan Shaw: StockSense", 
    page_icon=os.path.join("assets", "stocksense-favicon.png"),
    layout="centered", 
    initial_sidebar_state="collapsed"
)

#hide the hamburger menu
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
    st.error("Feature unavailable")
st.subheader("How it works?")