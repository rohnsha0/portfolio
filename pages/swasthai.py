import time

import streamlit as st
from PIL import Image
import os
from assets.swasthai import diseaseData

# set page title, icon and layout
st.set_page_config(
    page_title="Rohan Shaw: SwasthAI",
    page_icon=os.path.join("assets", "swasthai", "swasthai-favicon.png"),
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

st.image(os.path.join("assets", "swasthai", "swasthai_banner.png"))

st.toast("The android application is still under process. Contrubutions are welcome.")

with st.sidebar:
    st.subheader("Contents in the page")
    st.write("Click on the links below to navigate to the respective section.")
    st.write(
        """
        - [About SwasthAI](#about-swasthai)
        - [Features](#features)
            - [Scan](#scan)
            - [Care+](#care)
            - [mAI](#mai)
            - [Community](#community)
        - [How it works?](#how-it-works)
            - [Data Collection](#data-collection)
            - [Data Preparation & Model Training](#data-preparation--model-training)
            - [Model Evaluation](#model-evaluation)
        - [Contributions](#contributions)    
        """
    )

st.title('About SwasthAI')
with st.container(border=True):
    s1, s2, s3= st.columns(3)
    with s1:
        st.write("**Updated:** ___")
    with s2:
        st.write("**Version:** ___")
    with s3:
        st.write("**Developer:** Rohan Shaw")
instructions = """
        Either upload your own image or select from
        the sidebar to get a preconfigured image.
        The image you select or upload will be fed
        through the Deep Neural Network in real-time
        and the output will be displayed to the screen.
        """
st.write(instructions)
st.link_button(label="View on Github", type="primary", url="https://github.com/rohnsha0/SwasthAI")
selected_option = ""
sub_selected_option = ""

st.header("Features")
st.write("Info about the features of the app.")

st.subheader("Scan")
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
    file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if file:
        isPredicting = False
        col1, col2 = st.columns(2)
        with col1:
            st.image(Image.open(file).resize((256, 256)))
        with col2:
            dropdown_options = list(diseaseData.diseases.keys())
            selected_option = st.selectbox("Select Domain Model:", dropdown_options, index=None,
                                           placeholder="Unselected",
                                           help="Used for selecting the domain model to be used for scanning the image.")

            sub_dropdown = diseaseData.diseases.get(selected_option, [])
            sub_selected_option = st.selectbox("Select Model Varient", sub_dropdown, index=None,
                                               placeholder="Unselected",
                                               help="Used for selecting the model varient to be used for scanning the image.")

            isPredicting = st.button("Scan")
            print(f"predictionStatus: {isPredicting}, selected_option: {selected_option}")
            if isPredicting:
                if selected_option and sub_selected_option is None: st.error(
                    "Please select an option to scan the image.")

        if selected_option and sub_selected_option is not None and isPredicting:
            progress = st.progress(0, text="Checking if the uploaded image is valid")
            time.sleep(2)
            progress.progress(50, text="Testing")
            time.sleep(2)
            progress.progress(100, "Processed")
            st.error("Feature not yet available.")
            #st.subheader("Results")
            #st.write("Results will be displayed here.")

st.warning(
    'All features below are only exclusive on the **[mobile application](https://github.com/rohnsha0/SwasthAI-androidApp)**.')

st.subheader("Care+")
st.write("""
    It has a bunch of smaller but useful features included into the app that are designed to help users in their day-to-day life. Some of which are included below:\n
    - Get suggested health recommendations based on your recent scan, our knowledge base about you, and your past medical history.
    - Track your daily calorie intake by just scanning the food you eat and we will take care of the rest. Alternatively, you can also manually enter the food you eat.
    - Get yourself a personalized diet plan based on your recent scan, your past medical history, and your daily calorie intake.\n
    Apart from these, there are a lot of other features included in the app that are designed to help users in their day-to-day life like contents aimed to educate, spread awareness, etc.
""")

st.subheader("mAI")
st.write("""
    Our app's Chatbot feature serves as a convenient and accessible resource for users to inquire about health-related queries or obtain information about their recent scans. With natural language processing capabilities, users can seamlessly interact with the Chatbot by typing or speaking their questions, receiving prompt and accurate responses. 
    \nWhether seeking advice on symptoms, medication, or general health concerns, or wanting to understand the results of recent scans or medical tests, users can rely on the Chatbot to provide relevant information and guidance. 
""")
with st.expander("How does it help?"):
    st.error("Feature not yet available.")
st.write(
    "The Chatbot enhances user experience by offering personalized assistance, facilitating informed decision-making, and empowering users to take proactive steps towards managing their health effectively within the app's ecosystem.")

st.subheader("Community")
st.write("""
    Our engaging community provides users with a platform to post medical-related queries and receive responses from fellow community members. Users can easily compose their queries, categorize them for better organization, and submit them for feedback. 
    \nThrough engaging with queries by offering responses, upvoting helpful comments, and flagging inappropriate content, users foster a supportive environment where they can seek advice, share experiences, and offer assistance to one another regarding health-related concerns.
""")

st.header("How it works?")
st.write("""
    Your medical images like X-rays and MRIs are fed into a special kind of AI called a "Convolutional Neural Network" (CNN). Imagine this network as a web of interconnected neurons, much like the human brain. But instead of thoughts, these neurons process visual information. 
    \nHere's the magic: these neurons have been trained on massive datasets of labeled medical images, learning to recognize patterns linked to specific diseases. Just like doctors identify pneumonia in X-rays, our CNNs do the same, automatically extracting those crucial clues. 
    \nThink of it this way: when you feed in a new image, the CNN analyzes it, calculates the probability of each possible disease, and presents it like a scorecard. It doesn't diagnose, but helps doctors see potential issues they might miss.
""")
st.subheader("Data Collection")
st.write("Data for training the model was primarily collected from kaggle, and other open-source platforms and might be subjected to change in the future. Other than that,  for some specific diseases (like Pneumonia, Tuberculosis, etc) data was collected from other publicly available datasets other than from kaggle.")
st.subheader("Data Preparation & Model Training")
st.write("Since, the data collected was not upto the mark, it was augmented (i.e. Randomly flipped and rotated) to increase the size of datasets. After which the images are resized to 256x256 and then fed into the model for training. Below is the architecture of the model used for training the data.")
st.code(
    """
        Model: "sequential_6"
        _________________________________________________________________
        Layer (type)                Output Shape              Param #   
        =================================================================
        sequential_1 (Sequential)   (None, 256, 256, 3)       0         
                                                                        
        conv2d_24 (Conv2D)          (32, 256, 256, 64)        256       
                                                                        
        max_pooling2d_24 (MaxPoolin  (32, 128, 128, 64)       0         
        g2D)                                                            
                                                                        
        conv2d_25 (Conv2D)          (32, 128, 128, 64)        4160      
                                                                        
        max_pooling2d_25 (MaxPoolin  (32, 64, 64, 64)         0         
        g2D)                                                            
                                                                        
        conv2d_26 (Conv2D)          (32, 62, 62, 64)          36928     
                                                                        
        max_pooling2d_26 (MaxPoolin  (32, 31, 31, 64)         0         
        g2D)                                                            
                                                                        
        conv2d_27 (Conv2D)          (32, 30, 30, 64)          16448     
                                                                        
        max_pooling2d_27 (MaxPoolin  (32, 15, 15, 64)         0         
        g2D)                                                            
                                                                        
        conv2d_28 (Conv2D)          (32, 14, 14, 64)          16448     
                                                                        
        max_pooling2d_28 (MaxPoolin  (32, 7, 7, 64)           0         
        g2D)                                                            
                                                                        
        conv2d_29 (Conv2D)          (32, 6, 6, 64)            16448     
                                                                        
        max_pooling2d_29 (MaxPoolin  (32, 3, 3, 64)           0         
        g2D)                                                            
                                                                        
        flatten_4 (Flatten)         (32, 576)                 0         
                                                                        
        dense_8 (Dense)             (32, 64)                  36928     
                                                                        
        dense_9 (Dense)             (32, 2)                   130       
                                                                        
        =================================================================
        Total params: 127,746
        Trainable params: 127,746
        Non-trainable params: 0
        _________________________________________________________________
    """
)
st.write("The model was trained using the Adam optimizer with a learning rate of 0.001 and a batch size of 32. The model was trained for 15 epochs and was stopped by using early stoppage callback in tensorflow.")

st.subheader("Model Evaluation")
st.write("The trained model was trained upon 10% of the complete dataset and all metrics were given based upon this tests. The model was evaluated using the following metrics: Accuracy, Precision, Recall, F1-Score, ROC-AUC, and plotting the confusion matrix.")
st.header('Contributions')
st.write("""
    The project is open-source and is available on GitHub. You can contribute to the project by forking the repository and then creating a pull request. The project is open to all kinds of contributions i.e. bug fixes, feature addition, documentation, etc.
    \nPost to the issues for any bugs, feature requests or any discussions about either [web](https://github.com/rohnsha0/SwasthAI  ) or [android app](https://github.com/rohnsha0/SwasthAI-androidApp) version of the project.
""")