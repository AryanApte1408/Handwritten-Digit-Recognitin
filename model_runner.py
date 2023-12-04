import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input

def load_and_predict(input_image_path):
    # Load the trained model
    model = tf.keras.models.load_model('mnist-model')

    # Load and preprocess the input image
    input_image = (input_image_path)

    # Make a prediction
    result = model.predict(input_image)

    # Get the predicted class
    predicted_class = int(np.argmax(result))

    return predicted_class


