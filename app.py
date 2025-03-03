import streamlit as st
import pytesseract
from PIL import Image
from pdf2image import convert_from_bytes
import io
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Title of the appsss
st.title("Document OCR Extractor")

# Upload a file
uploaded_file = st.file_uploader("Upload a document (PDF, JPG, PNG)", type=["pdf", "jpg", "png"])

if uploaded_file is not None:
    file_extension = uploaded_file.name.split(".")[-1].lower()

    if file_extension == "pdf":
        # Convert PDF to images
        images = convert_from_bytes(uploaded_file.read())
        st.image(images[0], caption="First page of uploaded PDF", use_container_width=True)
        extracted_text = "\n".join(pytesseract.image_to_string(img) for img in images)

    else:  # For JPG and PNG
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)
        extracted_text = pytesseract.image_to_string(image)

    # Display extracted text
    st.subheader("Extracted Text:")
    st.text_area("Text Output", extracted_text, height=300)

    # Option to download extracted text
    st.download_button(
        label="Download Extracted Text",
        data=extracted_text,
        file_name="extracted_text.txt",
        mime="text/plain",
    )
