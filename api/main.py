# frontend/main.py

import requests
import streamlit as st
from PIL import Image

# https://discuss.streamlit.io/t/version-0-64-0-deprecation-warning-for-st-file-uploader-decoding/4465
st.set_option("deprecation.showfileUploaderEncoding", False)

# defines an h1 header
st.title("Dogbreed detection web app")

# displays a file uploader widget
image = st.file_uploader("Choose an image")

# displays a button
if st.button("Style Transfer"):
    if image is not None :
        files = {"file": image.getvalue()}
        st.image(image, width=500)
        res = requests.post(f"http://backend:8080/{style}", files=files)
        st.header(res)