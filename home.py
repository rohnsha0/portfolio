import streamlit as st
import os
from st_pages import show_pages_from_config

show_pages_from_config()

profile_pic = os.path.join("assets", "round_img.png")
PAGE_TITLE = "Digital CV | John Doe"
NAME = "Rohan Shaw"
DESCRIPTION = """
A budding tech enthusiast diving into Data Science and Android Development.
"""
CSS_FILE= os.path.join("assets", 'styles.css')


st.set_page_config(
    page_title="Rohan Shaw: Digital CV", 
    page_icon=profile_pic, 
    layout="centered", 
    initial_sidebar_state="collapsed"
)

with open(CSS_FILE) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open("assets/resume.pdf", "rb") as file:
    PDFbyte = file.read()

#hide the hamburger menu
hide_decoration_bar_style = '''<style>header {visibility: hidden;}</style>'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name="RohanShaw(Resume).pdf",
        mime="application/octet-stream",
    )
    #st.write("📫", EMAIL)

# --- SKILLS ---
st.write('\n')
st.header("Personal Skillset")
st.write("I have my skillsets divided into two categories: Data Science and Android Development.")
st.subheader("Data Science")
st.write(
    """
- Have intermediate knowledge of **Python**, and **SQL**
- Used libraries like **pandas**, **numpy**, **matplotlib**, **seaborn**, etc for data analysis and visualization and libraries like **tensorflow**, **keras**, etc for machine learning and deep learning.
- Used **SQL-lite** database for implementation in android clients and **no-SQL** database for firebase storage\n
*(Used **CNN**, **Web Scraping**, **NLP** in SwasthAI, & **Time Series forcasting** in StockSense)*
"""
)
st.subheader("Android Development")
st.write(
    """
- I have worked on xml as well as jetpack compose for the development of core elements in android development projects.
- I have used android libraries like retrofit, room, etc for API calls and database management respectively. Also, I have been using MVVM architecture for the development of android applications.\n
*(Used XML in SwasthAI, & Jetpack Compose in StockSense)*
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.header("Projects & Accomplishments")
st.write("Below are some of the projects I have worked on in the past. ")
# --- JOB 1
st.subheader("SwasthAI: AI-Doctor")
st.write(
    """
- Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
- Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
- Redesigned data model through iterations that improved predictions by 12%
"""
)
st.link_button("Learn More", "/swasthai", type="primary")

# --- JOB 2
st.write('\n')
st.subheader("StockSense: Analyze and Predict")
st.write(
    """
- Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%
- Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
- Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
"""
)
st.link_button("Learn More", "/swasthai", type="primary")