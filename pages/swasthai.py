import streamlit as st
from PIL import Image
import os

st.set_page_config(
    page_title="Rohan Shaw: SwasthAI", 
    page_icon="https://i.postimg.cc/zfjkwzPq/swasth-AILogo.png", 
    layout="centered", 
    initial_sidebar_state="collapsed"
)

hide_decoration_bar_style = '''<style>header {visibility: hidden;}</style>'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

st.image(os.path.join("styles", "swasthai_banner.png"))
st.title('About Project SwasthAI')
instructions = """
        Either upload your own image or select from
        the sidebar to get a preconfigured image.
        The image you select or upload will be fed
        through the Deep Neural Network in real-time
        and the output will be displayed to the screen.
        """
st.write(instructions)
st.link_button(label="View on Github", type="primary", url="https://github.com/rohnsha0/SwasthAI")
selected_option=""

st.sidebar.title("Scan Options")
dropdown_options = ["Lungs", "Brain"]

st.header("Scan")
st.write("""
    The flagship feature of the project where users can upload photocopy of their recent scan i.e. xray, mri, skin, etc to get 
    a ai-based prediction about what might gone wrong with the body part. 
""")
with st.expander("Get an hands-on experience on how the scanning and disease prediction works."):
    st.write("""
        Either upload your own image or select from
        the sidebar to get a preconfigured image.
        The image you select or upload will be fed
        through the Deep Neural Network in real-time. 
        \nWe don't collect any of the uploaded images for any any purpose including training, survallieance, etc.
    """)
    file= st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if(file):
            isPredicting= False
            col1, col2 = st.columns(2)
            with col1:
                st.image(Image.open(file).resize((256, 256)))
            with col2:
                    selected_option = st.selectbox("Select Domain Model:", dropdown_options, index=None, placeholder="Unselected", help="Used for selecting the domain model to be used for scanning the image.")
                    isPredicting=st.button("Scan")
                    print(f"predictionStatus: {isPredicting}, selected_option: {selected_option}")
                    if isPredicting: 
                        if selected_option is None: st.error("Please select an option to scan the image.")
            
            if selected_option is not None and isPredicting:
                st.info("Scanning...")
                st.subheader("Results")
                st.write("Results will be displayed here.")

st.subheader("How it works?")
st.write("""
    Your medical images like X-rays and MRIs are fed into a special kind of AI called a "Convolutional Neural Network" (CNN). Imagine this network as a web of interconnected neurons, much like the human brain. But instead of thoughts, these neurons process visual information. 
    \nHere's the magic: these neurons have been trained on massive datasets of labeled medical images, learning to recognize patterns linked to specific diseases. Just like doctors identify pneumonia in X-rays, our CNNs do the same, automatically extracting those crucial clues. 
    \nThink of it this way: when you feed in a new image, the CNN analyzes it, calculates the probability of each possible disease, and presents it like a scorecard. It doesn't diagnose, but helps doctors see potential issues they might miss.
""")

st.warning('All features below are only exclusive on the mobile application.')

st.header("Care+")
st.write("""
    It has a bunch of smaller but useful features included into the app
""")

st.header("mAI")
st.write("""
    Our app's Chatbot feature serves as a convenient and accessible resource for users to inquire about health-related queries or obtain information about their recent scans. With natural language processing capabilities, users can seamlessly interact with the Chatbot by typing or speaking their questions, receiving prompt and accurate responses. 
    \nWhether seeking advice on symptoms, medication, or general health concerns, or wanting to understand the results of recent scans or medical tests, users can rely on the Chatbot to provide relevant information and guidance. 
    \nThe Chatbot enhances user experience by offering personalized assistance, facilitating informed decision-making, and empowering users to take proactive steps towards managing their health effectively within the app's ecosystem.
""")

st.header("Community")
st.write("""
    Our engaging community provides users with a platform to post medical-related queries and receive responses from fellow community members. Users can easily compose their queries, categorize them for better organization, and submit them for feedback. 
    \nThrough engaging with queries by offering responses, upvoting helpful comments, and flagging inappropriate content, users foster a supportive environment where they can seek advice, share experiences, and offer assistance to one another regarding health-related concerns.
""")