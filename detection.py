# Import necessary libraries
import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load the pre-trained MNIST model
model = keras.models.load_model('mnist_model.h5')

# Load and preprocess the handwritten digit image
image = Image.open('handwritten_digit.png').convert('L')  # Load an image and convert it to grayscale
image = image.resize((28, 28))  # Resize the image to 28x28 pixels (MNIST input size)
image_array = np.array(image) / 255.0  # Normalize pixel values

# Reshape the image for model input
input_data = image_array.reshape(1, 28, 28)

# Perform digit recognition
predictions = model.predict(input_data)
predicted_digit = np.argmax(predictions)

# Display the recognized digit
plt.imshow(image_array, cmap='gray')
plt.title(f"Recognized Digit: {predicted_digit}")
plt.show()
