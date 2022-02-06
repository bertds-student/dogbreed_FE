# frontend/main.py

import requests
import streamlit as st
from PIL import Image

# https://discuss.streamlit.io/t/version-0-64-0-deprecation-warning-for-st-file-uploader-decoding/4465
st.set_option("deprecation.showfileUploaderEncoding", False)

# defines an h1 header
st.title("Hondenasiel.be - Hond zoekt nieuw baasje")
st.text("Registreer hier je hond voor adoptie. Vul de velden in en laadt zeker een foto op. Op basis hiervan bepalen we oa het ras.")
st.header("Honden info :")
naam_hond = st.text_input('Puk')
st.write('Naam : ', naam_hond)
leeftijd_hond = st.text_input('3,4')
st.write('Leeftijd (jaren) : ', leeftijd_hond)


# displays a file uploader widget
image = st.file_uploader("Laad hier een foto van je hond op : ")

# displays a button
if st.button("Bepaal het ras obv de foto"):
    if image is not None :
        files = {"file": image.getvalue()}
        st.image(image, width=500)
        res = requests.post(f"http://localhost:8080/upload/image", files=files)
        st.header(res)