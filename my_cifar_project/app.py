import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

# CIFAR-10 standard class labels
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

# Load the trained model
model = load_model("model/my_model.h5")  # Make sure this file is in the same folder

st.title("🧠 CIFAR-10 Image Classifier")
st.markdown("Upload a 32x32 image (or bigger) and get a prediction")

# Upload image
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Resize to 32x32 (CIFAR-10 input size)
    image = image.resize((32, 32))
    image_array = np.array(image) / 255.0
    input_array = image_array.reshape(1, 32, 32, 3)

    # Prediction
    prediction = model.predict(input_array)
    predicted_class = class_names[np.argmax(prediction)]

    st.success(f"✅ Predicted Label: {predicted_class}")
