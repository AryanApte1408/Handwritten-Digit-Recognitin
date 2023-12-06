from flask import Flask, request, render_template
import tensorflow as tf
import numpy as np
import json
import os

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

def load_model():
    # Load the trained model
    loaded_model = tf.keras.models.load_model('mnist-model')
    return loaded_model

# Load the model when the app starts
model = load_model()

@app.route('/')
def home():
    return render_template("email.html")

@app.route('/paint')
def paint():
    return render_template("paint.html")

@app.route('/infer', methods=['POST'])
def infer():
    data = np.array(request.json['input'])
    image = data.reshape((112, 112))[::4,::4].reshape((1, 28, 28))
    result = model.predict(image)
    predicted_class = int(np.argmax(result))
    return json.dumps({ 'result': predicted_class })
# model.py
import tensorflow as tf
import numpy as np

def load_model():
    # Load the trained model
    loaded_model = tf.keras.models.load_model('mnist-model')
    return loaded_model

def predict_digit(image_array):
    model = load_model()
    image = image_array.reshape((112, 112))[::4, ::4].reshape((1, 28, 28))
    result = model.predict(image)
    predicted_class = int(np.argmax(result))
    return predicted_class



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)


#meow aksjd,fgsal;idgukhas'dgha
#jsahdfjehfjehfjehfjefhjehf
