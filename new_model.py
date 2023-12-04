# model.py

import tensorflow as tf
import numpy as np
import cv2

def load_model():
    # Load the trained model
    loaded_model = tf.keras.models.load_model('mnist-model')
    return loaded_model

def preprocess_input_image(input_image_path):
    # Load the input image in grayscale
    img = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)
    
    # Resize the image to (28, 28) if needed
    img = cv2.resize(img, (28, 28))

    # Convert the image to a NumPy array and preprocess it
    img_array = np.expand_dims(img, axis=0)
    img_array = img_array / 255.0  # Normalize the pixel values to the range [0, 1]

    return img_array

def run_model_prediction(input_image):
    # Load the model
    model = load_model()

    # Process the input image
    image = preprocess_input_image(input_image)

    # Make a prediction
    result = model.predict(image)

    # Get the predicted class
    predicted_class = int(np.argmax(result))

    return predicted_class
