# test_new_model.py

from new_model import preprocess_input_image
from model_runner import load_and_predict

def test_load_and_predict():
    # Replace 'path/to/your/input_image.jpg' with the actual path to your input image for testing
    input_image_path = 'D:/Om data/Niit/Sem-7(Btech D.S.)/Capstone/Handwritten-Digit-Recognition-main/Handwritten-Digit-Recognition-main/test_image_8.jpg'

    # Perform prediction
    prediction = load_and_predict(preprocess_input_image(input_image_path))

    # Assert that the output is 8
    assert prediction == 8


test_load_and_predict()
