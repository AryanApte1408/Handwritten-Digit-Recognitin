import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input
from model_runner import load_and_predict

def load_and_preprocess_input(input_image_path):
    # Load the input image
    img = image.load_img(input_image_path, target_size=(28, 28))

    # Convert the image to a NumPy array
    img_array = image.img_to_array(img)

    # Expand dimensions to create a batch size of 1 and add a channel dimension
    img_array = np.expand_dims(img_array, axis=0)

    # Preprocess the image
    img_array = preprocess_input(img_array)

    return img_array

# Replace 'path/to/your/input_image.jpg' with the actual path to your input image
input_image_path = 'test image 7.jpg'

# Load and preprocess the input image
processed_image = load_and_preprocess_input(input_image_path)

# Perform prediction
prediction = load_and_predict(processed_image)

# Assert that the predicted class is 7
assert prediction == 7, f"Test Failed: Predicted class is {prediction}, expected 7"

# If the assertion passes, the test case will reach here
print("Test Passed: Predicted class is 7")
