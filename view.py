import streamlit as st
from PIL import Image

# Title of the app

st.title('Osteoporosis Detection')

st.write("Image Upload and Display")


# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Display the image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
    st.write("")
    st.write("Classifying...")
