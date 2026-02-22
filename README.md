🧠 CIFAR-10 Image Classifier

A deep learning web application that classifies images into 10 object categories from the CIFAR-10 dataset using a trained Convolutional Neural Network (CNN).
The model is deployed with an interactive Streamlit interface, allowing users to upload images and receive instant predictions.

🚀 Demo

Upload an image and the model will predict the object category in real time.

🖼️ Classes Supported

The model can recognize:

✈️ Airplane

🚗 Automobile

🐦 Bird

🐱 Cat

🦌 Deer

🐶 Dog

🐸 Frog

🐴 Horse

🚢 Ship

🚚 Truck

📂 Project Structure
my_cifar_project/
│
├── app.py                # Streamlit web application
├── model/
│   └── my_model.h5       # Trained CNN model
├── requirements.txt      # Dependencies
└── README.md             # Documentation
⚙️ How It Works

1️⃣ Upload an image (JPG/PNG/JPEG)
2️⃣ Image is resized to 32×32 pixels
3️⃣ Pixel values are normalized
4️⃣ CNN model predicts the class
5️⃣ Result is displayed instantly

🛠️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/yourusername/cifar10-classifier.git
cd cifar10-classifier
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Run the app
streamlit run app.py
🧪 Requirements

Python 3.x

TensorFlow / Keras

Streamlit

NumPy

Pillow

🎯 Use Cases

✅ Learning computer vision & CNNs
✅ Beginner deep learning deployment project
✅ Streamlit app deployment practice
✅ Educational demonstrations

📈 Future Improvements

Improve model accuracy

Show prediction confidence score

Display top-3 predictions

Deploy online (Streamlit Cloud)

Enhance UI design

🤝 Contributing

Contributions, suggestions, and improvements are welcome!

⭐ Acknowledgements

CIFAR-10 dataset creators

TensorFlow & Keras community

Streamlit for easy deployment
