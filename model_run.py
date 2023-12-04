import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input
from model_runner import load_and_predict
import cv2

def preprocess_input_image(input_image_path):
    # Load the input image in grayscale
    img = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)
    
    # Resize the image to (28, 28) if needed
    img = cv2.resize(img, (28, 28))

    # Convert the image to a NumPy array and preprocess it
    img_array = np.expand_dims(img, axis=0)
    img_array = img_array / 255.0  # Normalize the pixel values to the range [0, 1]

    return img_array

# Replace 'path/to/your/input_image.jpg' with the actual path to your input image
# input_image_path = 'path/to/your/input_image.jpg'
input_image_path = 'D:/Om data/Niit/Sem-7(Btech D.S.)/Capstone/Handwritten-Digit-Recognition-main/Handwritten-Digit-Recognition-main/test_image_8.jpg'


# Perform prediction
prediction = load_and_predict(preprocess_input_image(input_image_path))
print("Prediction-1:", prediction)
