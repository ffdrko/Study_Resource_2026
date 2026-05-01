import streamlit as st
from PIL import Image

st.title("Image to Grayscale Converter")

uploaded_file = st.file_uploader(
    "Upload an image file to convert to grayscale",
    type=["png", "jpg", "jpeg", "bmp", "gif", "webp"],
)

with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera")

if uploaded_file:
    img = Image.open(uploaded_file)
    gray_img = img.convert("L")
    st.subheader("Uploaded Image")
    st.image(img, use_column_width=True)
    st.subheader("Grayscale Image")
    st.image(gray_img, use_column_width=True)

elif camera_image:
    img = Image.open(camera_image)
    gray_img = img.convert("L")
    st.subheader("Camera Image")
    st.image(img, use_column_width=True)
    st.subheader("Grayscale Image")
    st.image(gray_img, use_column_width=True)