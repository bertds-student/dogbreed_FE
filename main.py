# frontend/main.py

import requests
import streamlit as st
from PIL import Image

# https://discuss.streamlit.io/t/version-0-64-0-deprecation-warning-for-st-file-uploader-decoding/4465
st.set_option("deprecation.showfileUploaderEncoding", False)

# defines an h1 header
st.title("Hondenasiel.be - Hond zoekt nieuw baasje")
image = Image.open(https://xxlfotobehang.nl/wp-content/uploads/2016/10/XXL-D-10.jpg)
st.image(image, caption='Deze honden hebben een goede thuis gevonden.')

st.Header("Honden info :")
naam_hond = st.text_input('Puk')
st.write('Naam : ', naam_hond)


# displays a file uploader widget
image = st.file_uploader("Laad hier een foto van je hond op : ")

# displays a button
if st.button("Bepaal het ras obv de foto"):
    if image is not None :
        files = {"file": image.getvalue()}
        st.image(image, width=500)
        res = requests.post(f"http://localhost:8080/upload/image", files=files)
        st.header(res)