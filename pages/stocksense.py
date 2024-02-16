import streamlit as st
import os

st.set_page_config(
    page_title="Rohan Shaw: StockSense", 
    page_icon=os.path.join("assets", "swasthai-favicon.png"),
    layout="centered", 
    initial_sidebar_state="collapsed"
)


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
st.write("""
    The flagship feature of the project where users can search for their preferred stocks to get a detailed idea for the future stock price. 
""")