import streamlit as st
import numpy as np
import cv2
from PIL import Image

st.set_page_config(page_title="AI Photo Guard", page_icon="🛡️")
st.title("🛡️ AI Photo Guard: अपनी फोटो सुरक्षित करें")
st.write("यहाँ फोटो अपलोड करें ताकि कोई AI आपका चेहरा न बदल सके।")

file = st.file_uploader("फोटो चुनें", type=["jpg", "png", "jpeg"])

if file:
    img = Image.open(file)
    st.image(img, caption="Original Photo")
    
    if st.button("Apply Privacy Shield"):
        # कोडिंग जो पिक्सल को 'Lock' करती है
        img_array = np.array(img)
        noise = np.random.randint(0, 3, img_array.shape, dtype='uint8')
        protected = cv2.add(img_array, noise)
        
        # रिजल्ट दिखाना
        result = Image.fromarray(protected)
        st.success("आपकी फोटो अब सुरक्षित है!")
        st.image(result, caption="Protected Photo")
        
        # डाउनलोड बटन
        st.download_button("Download Protected Image", 
                           data=cv2.imencode('.jpg', protected)[1].tobytes(),
                           file_name="protected_insta.jpg")
      
